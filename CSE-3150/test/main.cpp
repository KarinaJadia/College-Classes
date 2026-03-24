#include <iostream>
#include <vector>
#include <string>

int main() {
    std::cout << "Hello, Karina! 🎉 Your Clang++ setup works!\n";

    std::vector<std::string> words = {"C++", "with", "MSYS2", "and", "VS Code"};
    std::cout << "You are running: ";
    for (const auto& w : words) {
        std::cout << w << " ";
    }
    std::cout << std::endl;

    return 0;
}

// compile with ctrl + shift + b
// open mysys2 terminal
// cd /c/Users/karin/Music/CSE-3150/test/
// ./main.exe

// or cd /c/Users/karin/Music/CSE-3150/test/
// clang++ main.cpp