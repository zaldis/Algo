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
    The function that compare all symbols on 'str' from 'fromPref' and 'fromPattern'
    Complexity O(n)
*/
void naiveSearch(String str, int fromPref, int fromPattern, int to, int& matcher) {
    for (int itNext = fromPref; itNext < to - fromPattern; ++itNext) {
        if (str.at(itNext) == str.at(fromPattern + itNext)) {
            matcher++;
        } else {
            break;
        }
    }
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
    zfunc.assign(str.size() + 1, -1);

    int countMatch = 0;
    naiveSearch(str, 0, 1, str.size(), countMatch);

    zfunc[1] = countMatch;
    left = 1;
    right = countMatch;

    for (int ind = 2; ind < str.size(); ++ind) {
        countMatch = 0;
        if (ind >= right) {
            naiveSearch(str, 0, ind, str.size(), countMatch);
            zfunc[ind] = countMatch;
            if (countMatch > 0) {
                left = ind;
                right = ind + countMatch;
            }
        } else {
            int lastLength = right - ind + 1;
            if (zfunc[ind - left + 1] <= lastLength) {
                zfunc[ind] = zfunc[ind - left + 1];
            } else {
                zfunc[ind] = lastLength;
            }

            naiveSearch(str, right - left, right, str.size(), countMatch);

            zfunc[ind] = countMatch;
            if (countMatch > 0) {
                left = ind;
                right = ind + zfunc[ind];
            }
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