#include <iostream>
#include <string>
#include <vector>

typedef std::string String;
typedef std::vector<int> VInt;

void read(std::istream& in, String& input) {
    in >> input;
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

void printResult(std::ostream& out, String source, VInt prefixFunction) {
    for (int it = 0; it < prefixFunction.size(); ++it) {
        out << it << ": " << "(" << prefixFunction[it] << ")" << std::endl;

        if (prefixFunction[it] == 0) {
            out << "-" << std::endl << std::endl;
            continue;
        }

        for (int ind = 0; ind < prefixFunction[it]; ++ind) {
            out << source[ind];
        }

        out << "  ";

        for (int ind = prefixFunction[it]; ind <= it - prefixFunction[it]; ++ind) {
            out << source[ind];
        }

        out << "  ";

        for (int ind = it - prefixFunction[it] + 1; ind <= it; ++ind) {
            out << source[ind];
        }

        out << std::endl << std::endl;
    }
}

int main() {
    String str;
    read(std::cin, str);

    VInt prefixFunction;
    initPrefixFunction(str, prefixFunction);

    printResult(std::cout, str, prefixFunction);

    return 0;
}