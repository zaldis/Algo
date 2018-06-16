#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

struct Palindrom {
	size_t from;
	size_t size;

	Palindrom(size_t from, size_t size) {
		this->from = from;
		this->size = size;
	}
};

struct Node {
	size_t palindromSize;
	vector<Node*> childs;
	Node* suffixLink;

	Node() {
		palindromSize = 0;
		suffixLink = nullptr;
	}

	Node(size_t palindromSize) {
		this->palindromSize = palindromSize;
		suffixLink = nullptr;
	}
};

struct PalindromTree {
	Node* evenHead;
	Node* oddHead;
	Node* tail;

	PalindromTree() {
		evenHead = new Node();
		oddHead = new Node();

		evenHead->suffixLink = evenHead;
		
		oddHead->palindromSize = 1;
		oddHead->suffixLink = evenHead;

		tail = oddHead;
	}

	vector<Palindrom*> SearchPalindroms(const string& text) {
		vector<Palindrom> palindroms;
		palindroms.push_back(Palindrom(0, 1));

		for (int ind = 1; ind < text.size(); ++ind) {
			char symbol = text[ind];

			while (true) {
				if (text[ind - tail->palindromSize] == symbol) {
					size_t newPalindromSize = tail->palindromSize + 2;
					palindroms.push_back(Palindrom(ind, newPalindromSize));
					tail->childs.push_back(new Node(newPalindromSize));

					break;
				}

				if (tail == evenHead) {


					break;
				}

				tail = tail->suffixLink;
			}
		}
	}
};

int main() {

	
	return 0;
}