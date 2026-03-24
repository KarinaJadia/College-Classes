#include <set>
#include <vector>
#include <iostream>
using namespace std;

int ECSumList(const set<int> &listNums)
{
  // your code goes here ...

  // indexing
  int sum = 0;
  for (set<int>::const_iterator it = listNums.begin(); it != listNums.end(); ++it) {
      sum += *it;
  }
  return sum;

  // range
  int sum = 0;
  for (int num : listNums) {
      sum += num;
  }
  return sum;
}

// Test your code with this main function

int main()
{
  set<int> ss;
  ss.insert(5);
  ss.insert(3);
  ss.insert(3);
  ss.insert(0);
  ss.insert(1);
  int sum = ECSumList(ss);
  cout << "sum: " << sum << endl;
}