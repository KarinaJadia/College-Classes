// Starter code
#include <string>
#include <iostream>

std::string ECSwapCase(std::string str)
{
  // your code here...
  for (char &c : str) {
    if (std::islower(c)) {
      c = std::toupper(c);
    } else if (std::isupper(c)) {
      c = std::tolower(c);
    }
  }
  return str;
}

