#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::vector;
using std::string;

vector<int> GetOdd(const string& text) {
    const int textSize = text.size();
    vector<int> oddPalindrome(textSize, 0);

    int leftBlock = 0;
    int rightBlock = -1;
    int countPalindroms = 0;

    for (int ind = 0; ind < textSize; ++ind) {
        if (ind > rightBlock) {
            countPalindroms = 0;
        } else {
            countPalindroms = std::min(oddPalindrome[leftBlock + rightBlock - ind], rightBlock - ind) + 1;
        }

        while ( (ind + countPalindroms < textSize) && (ind - countPalindroms >= 0) ) {
            if (text[ind + countPalindroms] == text[ind - countPalindroms]) {
                countPalindroms++;
            } else {
                break;
            }
        }

        oddPalindrome[ind] = countPalindroms;
        countPalindroms--;

        if (ind + countPalindroms > rightBlock) {
            leftBlock = ind - countPalindroms;
            rightBlock = ind + countPalindroms;
        }
    }

    return oddPalindrome;
}

vector<int> GetEven(const string& text) {
    const int textSize = text.size();
    vector<int> evenPalindroms(textSize, 0);

    int leftBlock = 0;
    int rightBlock = -1;
    int countPalindroms = 0;

    for (int ind = 1; ind < textSize; ++ind) {
        if (ind > rightBlock) {
            countPalindroms = 0;
        } else {
            countPalindroms = std::min(evenPalindroms[leftBlock + rightBlock - ind + 1], rightBlock - ind + 1) + 1;
        }

        while (ind + countPalindroms - 1 < textSize && ind - countPalindroms >= 0) {
            if (text[ind + countPalindroms - 1] == text[ind - countPalindroms]) {
                countPalindroms++;
            } else {
                break;
            }
        }

        countPalindroms--;
        evenPalindroms[ind] = std::max(countPalindroms, 0);

        if (ind + countPalindroms - 1 > rightBlock) {
            leftBlock = ind - countPalindroms;
            rightBlock = ind + countPalindroms - 1;
        }
    }

    return evenPalindroms;
}

void PrintPalindroms(std::ostream& out, const string& text, const vector<int>& palindromsOdd, const vector<int>& palindromsEven) {
    out << "Text: " << text << std::endl;

    out << "================================= Odd palindroms" << std::endl;
    for (int center = 0; center < palindromsOdd.size(); ++center) {
        const int countPalindroms = palindromsOdd[center];
        out << "Center " << center << ": ";
        for (int it = center - countPalindroms + 1; it < center + countPalindroms; ++it) {
            out << text[it];
        }
        out << std::endl;
    }
    out << "================================= Odd palindroms" << std::endl;

    out << "================================= Even palindroms" << std::endl;
    for (int centerRight = 1; centerRight < palindromsEven.size(); ++centerRight) {
        const int countPalindroms = palindromsEven[centerRight];
        out << "Center right " << centerRight << ": ";
        if (palindromsEven[centerRight] == 0) {
            out << "-";
        } else {
            for (int it = centerRight - countPalindroms; it < centerRight + countPalindroms; ++it) {
                out << text[it];
            }
        }
        out << std::endl;
    }
    out << "================================= Even palindroms" << std::endl;
}

int main() {
    // string text = "akakaakaka";
    // string text = "papapapap";
    // string text = "abbaabba";
    string text = "abcdeff";
    vector<int> palindromsOdd = GetOdd(text);
    vector<int> palindromsEven = GetEven(text);

    PrintPalindroms(std::cout, text, palindromsOdd, palindromsEven);

    return 0;
}