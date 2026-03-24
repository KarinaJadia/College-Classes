#include <vector>
#include <iostream>
using namespace std;

// return the sum of the numbers
int ECSumList(const vector<int> &listNums)
{
  // your code goes here ...

  // indexing
  int sum = 0;
  for (size_t i = 0; i < listNums.size(); i++) {
      sum += listNums[i];
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
  vector<int> vec;
  vec.push_back(2);
  vec.push_back(3);
  vec.push_back(3);
  vec.push_back(0);
  vec.push_back(1);
  int sum = ECSumList(vec);
  cout << "sum: " << sum << endl;
}
