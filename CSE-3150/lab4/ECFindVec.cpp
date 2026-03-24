#include <vector>
#include <iostream>
#include <ctime>
using namespace std;

bool ECFind(const vector<int> &listVecs, int x)
{
  // your code here
}

// Test your code with this main function

int main()
{
  // create a list of certain size
  const int NUM_INTS = 10000;
  vector<int> vec;
  for(int i=0; i<NUM_INTS; ++i)
  {
    vec.push_back(i);
  }
  const int NUM_FIND = 100000;

  auto start = clock();
  for(int i=0; i<NUM_FIND; ++i)
  {
    ECFind(vec,i);
  } 
  auto end = clock();
  double duration = static_cast<double>(end - start) / CLOCKS_PER_SEC;
  cout << "Time taken: " << duration << " seconds" << endl;
}

