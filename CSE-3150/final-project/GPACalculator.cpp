#include "GPACalculator.h"
#include <stdexcept>

GPACalculator::GPACalculator()
: gradePoints({
    {"A", 4.0}, {"A-", 3.7},
    {"B+", 3.3}, {"B", 3.0}, {"B-", 2.7},
    {"C+", 2.3}, {"C", 2.0}, {"C-", 1.7},
    {"D+", 1.3}, {"D", 1.0},
    {"F", 0.0}
}) {}

void GPACalculator::addCourse(const Course &c) {
    if (gradePoints.find(c.grade) == gradePoints.end()) {
        throw std::invalid_argument("Unknown grade string");
    }
    courses.push_back(c);
}

void GPACalculator::removeCourse(size_t index) {
    if (index < courses.size())
        courses.erase(courses.begin() + index);
}

std::vector<Course> GPACalculator::getCourses() const {
    return courses;
}

double GPACalculator::calculateSemesterGPA(const std::string &semester) const {
    double totalPoints = 0, totalCredits = 0;

    for (const auto &c : courses) {
        if (c.semester == semester) {
            totalPoints += c.credits * gradePoints.at(c.grade);
            totalCredits += c.credits;
        }
    }
    return totalCredits == 0 ? 0.0 : totalPoints / totalCredits;
}

double GPACalculator::calculateOverallGPA() const {
    double totalPoints = 0, totalCredits = 0;

    for (const auto &c : courses) {
        totalPoints += c.credits * gradePoints.at(c.grade);
        totalCredits += c.credits;
    }
    return totalCredits == 0 ? 0.0 : totalPoints / totalCredits;
}

double GPACalculator::calculateMajorGPA(bool majorOnly) const {
    double totalPoints = 0, totalCredits = 0;

    for (const auto &c : courses) {
        if (c.isMajor == majorOnly) {
            totalPoints += c.credits * gradePoints.at(c.grade);
            totalCredits += c.credits;
        }
    }
    return totalCredits == 0 ? 0.0 : totalPoints / totalCredits;
}

double GPACalculator::creditsNeededForGoal(double goalGPA, double expectedGradePoint) const {
    double totalPoints = 0, totalCredits = 0;

    for (const auto &c : courses) {
        totalPoints += c.credits * gradePoints.at(c.grade);
        totalCredits += c.credits;
    }

    double denom = expectedGradePoint - goalGPA;
    if (denom == 0)
        return 1e9;

    double x = (goalGPA * totalCredits - totalPoints) / denom;
    return x < 0 ? 0.0 : x;
}

void GPACalculator::clear() {
    courses.clear();
}