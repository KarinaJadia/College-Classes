// Check if the string contains valid parentheses
// The string may include '(', ')', '[', ']' and other characters
// These parentheses must be properly matched e.g. (), [()], [([])]

#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool ECParenthesesCheck(const std::string& strInput)
{
    // Implement the ECParenthesesCheck function here...

    // using a stack to track openings/closing match
    vector<char> stack;
    for (char c : strInput) {
        if (c == '(' || c == '[') {
            stack.push_back(c);
        } 
        else if (c == ')' || c == ']') {
            if (stack.empty()) return false;
            char top = stack.back();
            stack.pop_back();
            if ((c == ')' && top != '(') || 
                (c == ']' && top != '[')) {
                return false;
            }
        }
    }

    return stack.empty(); // valid if nothing left unmatched
}
