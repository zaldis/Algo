/*
 *  The algorithm find substring in
 *  source string. Using prefix-function.
 *
 *  Complexity O(n)
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctime>

typedef std::string String;
typedef std::vector<int> VInt;

void read(std::istream& in, String& text, String& pattern) {
    in >> text >> pattern;
}

void initPrefixFunction(String source, VInt& prefixFunction) {
    int len = source.size();
    prefixFunction.assign(len, 0);

    for (int ind = 1; ind < len; ++ind) {
        int nextInd = prefixFunction[ind - 1];
        while (nextInd > 0 && source[ind] != source[nextInd]) {
            nextInd = prefixFunction[nextInd - 1];
        }

        if (source[ind] == source[nextInd]) {
            prefixFunction[ind] = nextInd + 1;
        }
    }
}

VInt indexesOf(String text, String pattern) {
    VInt prefixFunction;
    String source = pattern + "~" + text;

    initPrefixFunction(source, prefixFunction);

    VInt answer;
    for (int ind = 0; ind < text.size(); ++ind) {
        if (prefixFunction[ind + pattern.size() + 1] == pattern.size()) {
            answer.push_back(ind - pattern.size() + 1);
        } 
    }

    return answer;
}

void printResult(std::ostream& out, const String text, const String pattern, VInt const& indexes, const clock_t times) {
    out << "Text: " << text << std::endl;
    out << "Pattern: " << pattern << std::endl;

    out << "Time: " << times << std::endl;

    for (auto index : indexes) {
        out << index << " ";
    }
    out << std::endl;
}

int main() {
    String text;
    String pattern;
    std::ifstream input("input.txt");
    read(input, text, pattern);

    const clock_t timeBegin = std::clock();
    VInt indexes = indexesOf(text, pattern);
    const clock_t timeEnd = std::clock();

    printResult(std::cout, text, pattern, indexes, timeEnd - timeBegin);

    return 0;
}