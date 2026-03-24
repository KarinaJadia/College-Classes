#pragma once
#include <vector>
#include <string>
#include <map>

struct Course {
    std::string name;
    std::string semester;
    double credits;
    std::string grade;
    bool isMajor;
};

class GPACalculator {
public:
    GPACalculator();
    void addCourse(const Course &c);
    void removeCourse(size_t index);
    std::vector<Course> getCourses() const;

    double calculateSemesterGPA(const std::string &semester) const;
    double calculateOverallGPA() const;
    double calculateMajorGPA(bool majorOnly) const;
    double creditsNeededForGoal(double goalGPA, double expectedGradePoint) const;

    void clear();

private:
    std::vector<Course> courses;
    std::map<std::string, double> gradePoints;
};