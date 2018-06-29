/*
 *  The 'Suffix Trie' is the data structure
 *  that saves all suffixes of input string.
 *  
 *  Usually used for searching substring in the string
 *
 *  Time complexity (building): O(n^2)
 *  Time complexity (searching): O(|pattern|)
 *  Memory complexity: O(n^2)
 *
*/

#include <iostream>
#include <vector>
#include <string>
#include <map>

using std::map;
using std::string;
using std::vector;

const char SENTINEL = '#';

struct Node {
    map<char, Node*> children;
};

class TrieSuffix {
    Node* root = NULL;
    Node* currentPosition = NULL;

    void Add(string text) {
        Node* current = root;

        for (char symbol : text) {
            if (current->children.find(symbol) == current->children.end()) {
                current->children[symbol] = new Node();
            }

            current = current->children[symbol];
        }
    }

public:
    void Build(string text) {
        root = new Node();
        int textSize = text.size();

        string suffix;
        for (int ind = 0; ind < textSize; ++ind) {
            suffix = text.substr(ind, textSize - ind);
            Add(suffix);
        }

        currentPosition = root;
    }

    bool NextStep(char symbol) {
        if (currentPosition->children.find(symbol) != currentPosition->children.end()) {
            currentPosition = currentPosition->children[symbol];
            return true;
        } else {
            ResetSearchPointer();
            return false;
        }
    }

    void ResetSearchPointer() {
        currentPosition = root;
    }
};

string ReadText(std::istream& in) {
    int countStrings;
    in >> countStrings;
    string text = "";

    string str;
    for (int ind = 0; ind < countStrings; ++ind) {
        in >> str;
        text += str + SENTINEL;
    }

    return text;
}

bool FindSubstring(TrieSuffix& trieSuffix, string substr) {
    trieSuffix.ResetSearchPointer();
    for (char symbol : substr) {
        if (!trieSuffix.NextStep(symbol)) {
            return false;
        }
    }

    return true;
}

void StartSearch(string sourceText, vector<string>& substrings, std::ostream& out) {
    TrieSuffix trieSuffix;
    trieSuffix.Build(sourceText);

    for (string substring : substrings) {
        out << FindSubstring(trieSuffix, substring) << " ";
    }
}

int main() {
    string text = ReadText(std::cin);
    vector<string> substrings = { "aaa", "ksljdf", "ccc" };
    StartSearch(text, substrings, std::cout);

    return 0;
}
