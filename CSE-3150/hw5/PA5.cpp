#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

// 1. Create Spiral Cipher Map
std::map<char, char> ECCreateSpiralCipherMap() {
    std::map<char, char> cipher;
    const int totalChars = 95;

    std::vector<char> chars;
    for (int i = 32; i <= 126; ++i) {
        chars.push_back(static_cast<char>(i));
    }

    int n = std::ceil(std::sqrt(totalChars));
    std::vector<std::vector<char>> grid(n, std::vector<char>(n, '\0'));

    int idx = 0;
    for (int i = 0; i < n && idx < totalChars; ++i) {
        for (int j = 0; j < n && idx < totalChars; ++j) {
            grid[i][j] = chars[idx++];
        }
    }

    std::vector<char> spiral;
    int top = 0, bottom = n - 1, left = 0, right = n - 1;

    while (top <= bottom && left <= right) {
        for (int j = left; j <= right; ++j)
            if (grid[top][j] != '\0') spiral.push_back(grid[top][j]);
        top++;

        for (int i = top; i <= bottom; ++i)
            if (grid[i][right] != '\0') spiral.push_back(grid[i][right]);
        right--;

        for (int j = right; j >= left && top <= bottom; --j)
            if (grid[bottom][j] != '\0') spiral.push_back(grid[bottom][j]);
        bottom--;

        for (int i = bottom; i >= top && left <= right; --i)
            if (grid[i][left] != '\0') spiral.push_back(grid[i][left]);
        left++;
    }

    for (int i = 0; i < (int)spiral.size(); ++i) {
        cipher[spiral[i]] = spiral[(i + 1) % spiral.size()];
    }

    return cipher;
}

// 2. Encrypt Message
std::string ECEncryptMessage(const std::string& msg, const std::map<char, char>& cipher) {
    std::string result;
    result.reserve(msg.size());

    for (char c : msg) {
        auto it = cipher.find(c);
        result += (it != cipher.end()) ? it->second : c;
    }

    return result;
}

// 3. Decrypt Message
std::string ECDecryptMessage(const std::string& encrypted, const std::map<char, char>& cipher) {
    std::map<char, char> reverseCipher;
    for (auto& pair : cipher) {
        reverseCipher[pair.second] = pair.first;
    }

    std::string result;
    result.reserve(encrypted.size());

    for (char c : encrypted) {
        auto it = reverseCipher.find(c);
        result += (it != reverseCipher.end()) ? it->second : c;
    }

    return result;
}

// 4. Character Frequency
std::map<char, int> ECCharacterFrequency(const std::string& msg) {
    std::map<char, int> freq;
    for (char c : msg) {
        freq[c]++;
    }
    return freq;
}

// 5. Common Characters
std::vector<char> ECCommonCharacters(const std::string& a, const std::string& b) {
    std::vector<char> common;
    std::string seen;

    for (char c : a) {
        if (b.find(c) != std::string::npos && seen.find(c) == std::string::npos) {
            common.push_back(c);
            seen += c;
        }
    }

    return common;
}


// Notes: you can run the code with the test cases provided in test-pa5.cpp
// command - g++ -std=c++17 -Wall -Wextra -o test test-pa5.cpp PA5.cpp