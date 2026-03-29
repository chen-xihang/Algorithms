#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

string longestPalindrome(const string& s) {
    if (s.empty()) return "";

    string t;
    t.reserve(2 * s.size() + 3);
    t.push_back('^');
    for (char c : s) {
        t.push_back('#');
        t.push_back(c);
    }
    t.push_back('#');
    t.push_back('$');

    vector<int> P(t.size(), 0);
    int center = 0, right = 0;
    int best_center = 0, best_radius = 0;

    for (int i = 1; i < (int)t.size() - 1; ++i) {
        int mirror = 2 * center - i;

        if (i < right) {
            P[i] = min(P[mirror], right - i);
        }

        while (t[i + P[i] + 1] == t[i - P[i] - 1]) {
            ++P[i];
        }

        if (i + P[i] > right) {
            center = i;
            right = i + P[i];
        }

        if (P[i] > best_radius) {
            best_radius = P[i];
            best_center = i;
        }
    }

    int start = (best_center - best_radius) / 2;
    return s.substr(start, best_radius);
}

int main() {
    std::cout << longestPalindrome("babad") << '\n';
    std::cout << longestPalindrome("cbbd") << '\n';
}