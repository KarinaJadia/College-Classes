#include <iostream>
#include <vector>
using namespace std;

bool ECIsIsomorphic(string s, string t);

int main()
{
    vector<string> strings1;
    vector<string> strings2;
    vector<bool> solutions;

    // Test 0
    strings1.push_back("egg");
    strings2.push_back("add");
    solutions.push_back(true);

    // Test 1 -- tests if mapping is one-to-one, a and r cannot both map to o
    strings1.push_back("foo");
    strings2.push_back("bar");
    solutions.push_back(false);

    // Test 2
    strings1.push_back("");
    strings2.push_back("");
    solutions.push_back(true);

    // Test 3
    strings1.push_back("ilovecpp");
    strings2.push_back("abcdefgg");
    solutions.push_back(true);

    // Test 4
    strings1.push_back("ilovecpp");
    strings2.push_back("function");
    solutions.push_back(false);

    for(int i = 0; i < strings1.size(); i++){
        bool funcOutput = ECIsIsomorphic(strings1[i], strings2[i]);
        cout << "Test " << i << ((funcOutput == solutions[i]) ? " Suceeded" : " Failed") << " with output: " << funcOutput << endl;
    }
    
    return 0;
}