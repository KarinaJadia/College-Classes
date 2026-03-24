#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "GPACalculator.h"

namespace py = pybind11;

PYBIND11_MODULE(gpa_module, m) {
    py::class_<Course>(m, "Course")
        .def(py::init<>())
        .def_readwrite("name", &Course::name)
        .def_readwrite("semester", &Course::semester)
        .def_readwrite("credits", &Course::credits)
        .def_readwrite("grade", &Course::grade)
        .def_readwrite("isMajor", &Course::isMajor);

    py::class_<GPACalculator>(m, "GPACalculator")
        .def(py::init<>())
        .def("addCourse", &GPACalculator::addCourse)
        .def("removeCourse", &GPACalculator::removeCourse)
        .def("getCourses", &GPACalculator::getCourses)
        .def("calculateSemesterGPA", &GPACalculator::calculateSemesterGPA)
        .def("calculateOverallGPA", &GPACalculator::calculateOverallGPA)
        .def("calculateMajorGPA", &GPACalculator::calculateMajorGPA)
        .def("creditsNeededForGoal", &GPACalculator::creditsNeededForGoal)
        .def("clear", &GPACalculator::clear);
}
