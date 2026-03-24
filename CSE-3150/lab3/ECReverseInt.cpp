//
//  ECReverseInt.cpp
//  
//
//  Created by Yufeng Wu on 11/13/19.
//  Reverse an integer. Assume unsigned.
//

#include <iostream>

using namespace std;

// Reverse an integer (stored in decimal format in a string)
string ECReverseInt(const string &strNumber)
{
    string res;

    // your code goes here

    for (int i = strNumber.size() - 1; i >= 0; --i) {
        res += strNumber[i];
    }

    size_t firstNonZero = res.find_first_not_of('0');
    res = res.substr(firstNonZero);
    
    return res;
}

int main()
{
    cout << ECReverseInt("1234") << endl;
    cout << ECReverseInt("4321") << endl;
    cout << ECReverseInt("3210") << endl;
    cout << ECReverseInt("1000") << endl;
    cout << ECReverseInt("1002") << endl;
}