#include <iostream>
using namespace std;

// a function to be called
void bar()
{
  int u = 3;
  cout << "u: " << u << endl;
}

// a simple function
void foo()
{
  int x = 1;
  cout << "x = " << x << endl;

  int *pz = new int;
  *pz = 2;
  cout << "pz points to: " << *pz << endl;
  delete pz;

  char arr[10] = "hello";
  cout << "arr = " << arr << endl;

  // call bar
  bar();
}

int main()
{
  foo();
}
