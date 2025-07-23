#include <iostream>
#include <string>
using namespace std;

int main(void) {
    string s = "PAYPALISHIRING";
    int numRows = 3;

    if (numRows == 1 || numRows >= s.length()) {
        cout << s;
        return 0;
    }

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

    cout << res;
    return 0;
}
