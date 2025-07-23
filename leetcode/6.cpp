#include <iostream>
#include <string>

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length())
            return s;

        string res = "";
        int increment = 2 * (numRows - 1);

        for (int r = 0; r < numRows; r++) {
            for (int i = r; i < s.length(); i += increment) {
                res += s[i];

                // For middle rows, add the diagonal character
                int diagIndex = i + increment - 2 * r;
                if (r > 0 && r < numRows - 1 && diagIndex < s.length()) {
                    res += s[diagIndex];
                }
            }
        }

        return res;
    }
};
