// Starter code
#include <iostream>

using namespace std;

string ECStringSep(const string &str)
{
  string res;
  // your code goes here
  for (size_t i = 0; i < str.size(); i++)
  {
      res += str[i];
      if (i != str.size() - 1)
          res += ",";
  }
  return res;
}

