#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using std::vector;
using std::string;

vector<int> MakePrefixFunction(const string& source) {
    int sourceLen = source.size();
    vector<int> prefixFunxtion(sourceLen, 0);

    for (int ind = 1; ind < sourceLen; ++ind) {
        int nextInd = prefixFunxtion[ind - 1];
        while (nextInd > 0 && source[ind] != source[nextInd]) {
            nextInd = prefixFunxtion[nextInd - 1];
        }

        if (source[ind] == source[nextInd]) {
            prefixFunxtion[ind] = nextInd + 1;
        }
    }

    return prefixFunxtion;
}

vector<vector<int>> MakeAutomation(const string& pattern, string alphabet)  {
    int patternLen = pattern.size();
    // maximum code size of symbols in alphabet
    int alphabetLen = 1000;
    vector<int> prefixFunction = MakePrefixFunction(pattern + "#");
    vector<vector<int>> matrixAutomation(
        patternLen + 1, 
        vector<int>(alphabetLen));

    for (int state = 0; state <= patternLen; ++state) {
        for (auto symbol : alphabet) {
            if (pattern[state] != symbol) {
                if (state == 0) {
                    matrixAutomation[state][symbol] = 0;
                } else {
                    matrixAutomation[state][symbol] =
                        matrixAutomation[prefixFunction[state - 1]][symbol];
                }
            }

            if (pattern[state] == symbol) {
                matrixAutomation[state][symbol] = state + 1;
            }
        }
    }

    return matrixAutomation;
}

string MakeAlphabet() {
    string alphabet = "";

    for (char symbol = 'a'; symbol <= 'z'; ++symbol) {
        alphabet.push_back(symbol);
    }

    return alphabet;
}

void PrintAutomation(std::ostream& out, string alphabet, const vector<vector<int>>& automation) {
    out << "=========================== Automation\n";

    for (char symbol : alphabet) {
        out << std::setw(5) << symbol << " ";
    }
    out << std::endl;

    for (char symbol : alphabet) {
        out << std::setw(5) << "-----" << " ";
    }

    out << std::endl;
    int stateId = 0;
    for (auto states : automation) {
        out << stateId++ << "| ";
        for (int ind = alphabet[0]; ind <= alphabet[alphabet.size() - 1]; ++ind) {
            if (ind == alphabet[0]) {
                out << std::setw(2) << states[ind] << " ";
            } else {
                out << std::setw(5) << states[ind] << " ";
            }
        }
        out << std::endl;
    }

    out << "===========================\n\n\n";
}

vector<int> FindSubstring(string text, const vector<vector<int>>& automation, const int termState) {
    const int textSize = text.size();
    int state = 0;
    vector<int> res;

    for (int ind = 0; ind < textSize; ++ind) {
        state = automation[state][text[ind]];
        if (state == termState) {
            res.push_back(ind);
        }
    }

    return res;
}

void PrintResult(std::ostream& out, string text, string pattern, vector<int> res, const int patternSize) {
    out << "=========================== Result\n";
    out << "Text: " << text << std::endl;
    out << "Pattren: " << pattern << std::endl;

    for (auto ind : res) {
        out << ind - patternSize + 1 << " ";
    }

    if (res.size() == 0) {
        out << -1;
    }

    out << "\n=========================== Result\n\n\n";
}

int main() {
    string alphabet = MakeAlphabet();
    string pattern = "";
    string text = "";
    vector<int> indexesOfSubstring;
    vector<vector<int>> automation;

    pattern = "papa";
    const int termState = pattern.size();
    automation = MakeAutomation(pattern, alphabet);
    PrintAutomation(std::cout, alphabet, automation);

    //// pattern = abaab
    //// Example 1
    //text = "ababaabaab";
    //indexesOfSubstring = FindSubstring(text, automation, termState);
    //PrintResult(std::cout, text, pattern, indexesOfSubstring, termState);

    //// pattern = abaab
    //// Example 2
    //text = "abaab";
    //indexesOfSubstring = FindSubstring(text, automation, termState);
    //PrintResult(std::cout, text, pattern, indexesOfSubstring, termState);

    //// pattern = abaab
    //// Example 3
    //text = "abaacb";
    //indexesOfSubstring = FindSubstring(text, automation, termState);
    //PrintResult(std::cout, text, pattern, indexesOfSubstring, termState);

    // Example 4
    text = "papapapa";
    indexesOfSubstring = FindSubstring(text, automation, termState);
    PrintResult(std::cout, text, pattern, indexesOfSubstring, termState);

    return 0;
}