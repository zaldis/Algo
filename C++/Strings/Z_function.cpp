/*
  Algothim that find the substring in the string. Complexity O(n) 
  Using Z-function
*/

#include <iostream>
#include <vector>
#include <string>

typedef std::vector<int> ZFunc;
typedef std::string String;

void readStrings(std::istream& in, String& str, String& pattern) {
    in >> str;  // input str
    in >> pattern; // substring that is found
}

/*
    The function that initialize Z-function.

    left - index of start last Z-block
    right - index of end last Z-block

    z[0] - incalculable

    1) initialize z[1] with naive algorithm
    2) for all next indexes:
           - if (index >= right):
               * start naive algorithm
           - else (left <= index && index <= right):
               * put calculated value in z[ind] (ind ... right)
               * start naive algorithm

    Complexity O(n), because on all steps 
    increasing left or right and algorithm is running while
    left and right less then 'n'.
*/
void initZFunction(String str, ZFunc& zfunc) {
    int left = 0, right = 0;
    zfunc.assign(str.size() + 1, 0);
    int len = str.size();

    int countMatch;

    for (int ind = 1; ind < str.size(); ++ind) {
        countMatch = 0;
		// if in Z-block
        if (ind <= right) {
            zfunc[ind] = std::min(zfunc[ind - left], right - ind + 1);
        }

		// naive algorithm
        while (ind + zfunc[ind] < len && str[zfunc[ind]] == str[ind + zfunc[ind]]) {
            zfunc[ind]++;
        }

		// if new Z-block over previously Z-block
        if (ind + zfunc[ind] - 1 > right) {
            left = ind;
            right = ind + zfunc[ind] - 1;
        }
    }
}

/*
    Return -1 if 'pattern' is not substring of 'str'
    Elsewhere return index of 'pattern' in 'str'

    For this concatenating: 'pattern' + '#' + 'str',
    where '#' - sentinel;
    Then using Z-function. If Z-function on index 'ind' return value
    that equals to size of 'pattern' then 'pattern' is in 'str'
    from index 'ind'
*/
int indexOf(String str, String pattern) {
    ZFunc zfunc;
    String search = pattern + "~" + str;

    initZFunction(search, zfunc);

    for (int ind = 0; ind < zfunc.size(); ++ind) {
        if (zfunc[ind] == pattern.size()) {
            return ind - pattern.size() - 1;
        }
    }

    return -1;
}

int main() {
    String str, pattern;
    readStrings(std::cin, str, pattern);

    std::cout << indexOf(str, pattern);

    return 0;
}