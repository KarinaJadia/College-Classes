#include <iostream>

using namespace std;

bool ECIsIsomorphic(string s, string t) {
    // Implement function here
    if (s.size() != t.size()) return false; // first test case

    // character mappings
    char mapST[256]; // s -> t
    char mapTS[256]; // t -> s
    for (int i = 0; i < 256; i++) {
        mapST[i] = 0;
        mapTS[i] = 0;
    }

    for (int i = 0; i < s.size(); i++) {
        char c1 = s[i];
        char c2 = t[i];

        // check if mapped
        if (mapST[(unsigned char)c1] != 0 && mapST[(unsigned char)c1] != c2) {
            return false;
        }
        if (mapTS[(unsigned char)c2] != 0 && mapTS[(unsigned char)c2] != c1) {
            return false;
        }

        // map if not mapped
        mapST[(unsigned char)c1] = c2;
        mapTS[(unsigned char)c2] = c1;
    }

    return true;
}