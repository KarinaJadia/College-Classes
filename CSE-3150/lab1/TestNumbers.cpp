#include <iostream>
#include <string>
#include <stdexcept>
#include "ECNumbers.h"
#include "ECCalculator.h"
using namespace std;

// to run:
// clang++ TestNumbers.cpp ECNumbers.cpp ECCalculator.cpp
// ./a.exe

int main()
{
  // read in an integer n
  std::cout << "enter an integer: ";
  int n;
  std::cin >> n;

  // print out the square of it
  // your code here
  std::cout << "square root: " << ECNumbers::ECSquareN(n) << std::endl;

  // print out 2n  
  // your code here
  std::cout << "double: " << ECNumbers::ECDoubleN(n) << std::endl;

  // print out 4 times of n by invoking ECCalculator's function
  // your code here
  std::cout << "four times: " << ECCalculator::ECFourTimesN(n) << std::endl;

  return 0;
}