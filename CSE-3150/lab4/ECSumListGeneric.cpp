#include <vector>
#include <set>
#include <iostream>
using namespace std;

// I want to have a generic function that can work with any types of numbers 
// AND any type of container. Is this possible?
int ECSumList(const vector<int> &listNums)
{
  // your code goes here ...
}

// Test your code with this main function

int main()
{
  vector<int> vec;
  vec.push_back(2);
  vec.push_back(3);
  vec.push_back(3);
  vec.push_back(0);
  vec.push_back(1);
  int sum = ECSumList(vec);
  cout << "sum1: " << sum << endl;

  set<double> ss;
  ss.insert(5.0);
  ss.insert(3.0);
  ss.insert(3.0);
  ss.insert(0.0);
  ss.insert(1.0);
  double sum2 = ECSumList(ss);
  cout << "sum2: " << sum2 << endl;
}
