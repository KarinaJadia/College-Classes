#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

// Forward declarations (no PA5.h needed)
std::map<char, char> ECCreateSpiralCipherMap();
std::string ECEncryptMessage(const std::string& msg, const std::map<char, char>& cipher);
std::string ECDecryptMessage(const std::string& encrypted, const std::map<char, char>& cipher);
std::map<char, int> ECCharacterFrequency(const std::string& msg);
std::vector<char> ECCommonCharacters(const std::string& a, const std::string& b);

void TestRoundTrip() {
    std::string msg = "C++ is cool!";
    auto cipher = ECCreateSpiralCipherMap();
    std::string encrypted = ECEncryptMessage(msg, cipher);
    std::string decrypted = ECDecryptMessage(encrypted, cipher);

    std::cout << "[Round-Trip Test]\n";
    std::cout << "Original:  " << msg << "\n";
    std::cout << "Encrypted: " << encrypted << "\n";
    std::cout << "Decrypted: " << decrypted << "\n";
    std::cout << (decrypted == msg ? " Passed\n\n" : " Failed\n\n");
}

void TestFrequency() {
    std::string msg = "C++ is cool!";
    auto freq = ECCharacterFrequency(msg);

    std::cout << "[Character Frequency Test]\n";
    for (const auto& [ch, count] : freq) {
        std::cout << "'" << ch << "' : " << count << "\n";
    }
    std::cout << "\n";
}

void TestCommonCharacters() {
    std::string a = "encrypted";
    std::string b = "decrypted";
    auto common = ECCommonCharacters(a, b);

    std::cout << "[Common Characters Test]\n";
    std::cout << "String A: " << a << "\n";
    std::cout << "String B: " << b << "\n";
    std::cout << "Common: ";
    for (char c : common) std::cout << c << " ";
    std::cout << "\n\n";
}

int main() {
    TestRoundTrip();
    TestFrequency();
    TestCommonCharacters();
    return 0;
}
