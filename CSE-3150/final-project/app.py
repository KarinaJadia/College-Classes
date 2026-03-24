from flask import Flask, render_template, request, redirect, url_for
import gpa_module

app = Flask(__name__)
calculator = gpa_module.GPACalculator()

def calculate_filtered_gpa(courses):
    """
    Calculate GPA for a list of courses using a temporary GPACalculator.
    """
    temp_calc = gpa_module.GPACalculator()
    for c in courses:
        temp_calc.addCourse(c)
    return temp_calc.calculateOverallGPA()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST" and "add_course" in request.form:
        try:
            name = request.form["name"]
            semester = request.form["semester"]
            credits = float(request.form["credits"])
            grade = request.form["grade"]
            is_major = request.form.get("isMajor") == "on"

            course = gpa_module.Course()
            course.name = name
            course.semester = semester
            course.credits = credits
            course.grade = grade
            course.isMajor = is_major

            calculator.addCourse(course)
            message = f"Course {name} added!"
        except Exception as e:
            message = str(e)

    filter_semester = request.args.get("semester", "")
    filter_major = request.args.get("major", "")

    filtered_courses = calculator.getCourses()
    if filter_semester:
        filtered_courses = [c for c in filtered_courses if c.semester == filter_semester]
    if filter_major:
        if filter_major.lower() == "yes":
            filtered_courses = [c for c in filtered_courses if c.isMajor]
        elif filter_major.lower() == "no":
            filtered_courses = [c for c in filtered_courses if not c.isMajor]

    filtered_gpa = calculate_filtered_gpa(filtered_courses)
    overall_gpa = f'{calculator.calculateOverallGPA():.2f}'

    return render_template(
        "index.html",
        message=message,
        overall_gpa=overall_gpa,
        filtered_gpa=f'{filtered_gpa:.2f}',
        courses=filtered_courses,
        filter_semester=filter_semester,
        filter_major=filter_major
    )

@app.route("/delete/<int:index>")
def delete_course(index):
    calculator.removeCourse(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
