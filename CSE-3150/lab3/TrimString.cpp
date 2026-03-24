#include <string>
#include <iostream>
using namespace std;

//function that modifies a string `x` so that after the function call, `x` contains only its prefix of **up to five characters**.
void TrimString(std::string &x)
{
  string res;
  for(unsigned int i=0; i<5 && i<x.size(); ++i)
  {
    res += x[i];
  }
  x = res;
}

int main()
{
    string s = "12345678Hello";
    TrimString(s);
    cout << s << endl;  // prints "Hello"
    return 0;
}