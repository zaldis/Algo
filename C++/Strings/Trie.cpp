/*
 * Trie. 
 * This is structure for efficiency storage
 * strings for string's algorithms
 *
 * Complexity: Time   O(n * log(k))
 *             Memory O(n)
*/

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using std::map;
using std::vector;
using std::string;

const char DEFAULT_SYMBOL = 0;

class Node {
    map<char, Node> children;
    bool isTerminal;

public:
    Node() {
        isTerminal = false;
    }

    map<char, Node>& getChildren() {
        return children;
    }

    void setTerminal(bool newTerminal) {
        isTerminal = newTerminal;
    }
};

void addPattern(Node* root, string pattern) {
    Node* node = root;

    for (int it = 0; it < pattern.size(); ++it) {
        char symbol = pattern[it];
        if (node->getChildren().find(symbol) == node->getChildren().end()) {
            node->getChildren()[symbol] = Node();
        }

        node = &(node->getChildren()[symbol]);
    }

    node->setTerminal(true);
}

int main() {
    Node root;

    string patternA = "he";
    string patternB = "she";
    string patternC = "his";
    string patternD = "hers";

    addPattern(&root, patternA);
    addPattern(&root, patternB);
    addPattern(&root, patternC);
    addPattern(&root, patternD);

    // ~ -> h -> e -> r -> s
    //        -> i -> s       
    //   -> s -> h -> e

    return 0;
}