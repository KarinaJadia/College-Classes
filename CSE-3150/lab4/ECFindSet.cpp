#include <vector>
#include <set>
#include <iostream>
#include <ctime>
using namespace std;

bool ECFind(const set<int> &listNums, int x)
{
  // your code
}

// Test your code with this main function

int main()
{
  // create a list of certain size
  const int NUM_INTS = 10000;
  set<int> ss;
  for(int i=0; i<NUM_INTS; ++i)
  {
    ss.insert(i);
  }
  const int NUM_FIND = 100000;
  auto start = clock();
  for(int i=0; i<NUM_FIND; ++i)
  {
    ECFind(ss,i);
  } 
  auto end = clock();
  double duration = static_cast<double>(end - start) / CLOCKS_PER_SEC;
  cout << "Time taken: " << duration << " seconds" << endl;
}

