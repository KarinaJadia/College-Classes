from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "gpa_module",
        ["gpa_module.cpp", "GPACalculator.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    ),
]

setup(
    name="gpa_module",
    version="0.0.1",
    ext_modules=ext_modules,
)
