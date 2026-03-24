#include <iostream>
#include <vector>
using namespace std;

int ECLongestConsecutive(vector<int>& nums);

int main()
{
    vector<vector<int>> testVectors;
    vector<int> solutions;

    // Test 0
    testVectors.push_back({2,20,4,10,3,4,5});
    solutions.push_back(4);
    
    // Test 1
    testVectors.push_back({0,3,2,5,4,6,1,1});
    solutions.push_back(7);

    // Test 2
    testVectors.push_back({0,3,7,2,5,8,4,6,0,1});
    solutions.push_back(9);

    // Test 3
    testVectors.push_back({});
    solutions.push_back(0);

    // Test 4
    testVectors.push_back({0,0,0,0,0});
    solutions.push_back(1);

    // Test 5
    testVectors.push_back({1,8,9,1,3,4,});
    solutions.push_back(2);
    

    for(int i = 0; i < testVectors.size(); i++){
        int funcOutput = ECLongestConsecutive(testVectors[i]);
        cout << "Test " << i << ((funcOutput == solutions[i]) ? " Succeded" : " Failed") << " with output: " << funcOutput << endl;
    }

    return 0;
}