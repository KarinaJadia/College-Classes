// Test code for computeFibonacci
// To build: c++ ECFibonacciTest.cpp -o test
// To test: ./test

#include <iostream>
using namespace std;

#include "ECFibonacci.cpp"

int main()
{
  // Test basic cases
  cout << "F(0) = " << computeFibonacci(0) << " (expected: 0)" << endl;
  cout << "F(1) = " << computeFibonacci(1) << " (expected: 1)" << endl;
  cout << "F(2) = " << computeFibonacci(2) << " (expected: 1)" << endl;
  cout << "F(3) = " << computeFibonacci(3) << " (expected: 2)" << endl;
  cout << "F(4) = " << computeFibonacci(4) << " (expected: 3)" << endl;
  cout << "F(5) = " << computeFibonacci(5) << " (expected: 5)" << endl;
  cout << "F(10) = " << computeFibonacci(10) << " (expected: 55)" << endl;
  cout << "F(15) = " << computeFibonacci(15) << " (expected: 610)" << endl;
  
  // Test larger values to check efficiency
  cout << "F(20) = " << computeFibonacci(20) << " (expected: 6765)" << endl;
  cout << "F(30) = " << computeFibonacci(30) << " (expected: 832040)" << endl;
  
  return 0;
}