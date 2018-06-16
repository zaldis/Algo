/*
 * Hash function for strings in ANSII incoding
 */

#include <iostream>
#include <string>

using std::string;

unsigned long HashString(string str) {
    unsigned long hash = 5381;
    char symbol;

    for (int ind = 0; ind < str.size(); ++ind) {
        symbol = str[ind];
        hash = ((hash << 5) + hash) + symbol;
    }

    return hash;
}

int main() {
    string a = "Hello";
    string b = "hello";
    string c = "ello";
    string d = "Hello";

    unsigned long hashA = HashString(a);
    unsigned long hashB = HashString(b);
    unsigned long hashC = HashString(c);
    unsigned long hashD = HashString(d);

    std::cout << "Hash " << a << ": " << hashA << std::endl;
    std::cout << "Hash " << b << ": " << hashB << std::endl;
    std::cout << "Hash " << c << ": " << hashC << std::endl;
    std::cout << "Hash " << d << ": " << hashD << std::endl;

    return 0;
}