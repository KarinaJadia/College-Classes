// You are tasked with creating a C++ program that will analyze two arrays of integers,
// referred to as "arrayA" and "arrayB," and determine how many times an integer in  
// "arrayA" occurs in "arrayB"

// The program should output "arrayC" that matches the length of "arrayA"
// the indicies of "arrayC" map to the same indicies of "arrayA" with the values
// representing the number of occurrences

// For example, if "arrayA" contains {1, 3} and "arrayB" contains 
// {2, 1, 6, 1, 10, 3, 7}, the program should output {2, 1}
// indicating that "1" from "arrayA" occurs twice and "3" occurs once

// Tip: don't reinvent the wheel; try to use C++ standard library functions

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


// Function to count the number of integers present in both arrays using binary search
std::vector<int> ECNumOccurrences(const std::vector<int>& arrayA, const std::vector<int>& arrayB) {
    std::vector<int> arrayC;
    
    
    // Your code goes here...

    for (int n : arrayA) {
        auto range = equal_range(arrayB.begin(), arrayB.end(), n);
        arrayC.push_back(distance(range.first, range.second));
    }

    return arrayC;
}


