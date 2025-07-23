#include <iostream>
#include <string>
using namespace std;

int main(){
    string s = "racecar";

    int resLen=0;
    string res="";

    for(int i=0;i<s.size();i++){
        

        //odd length palindrome

        int l=i,r=i;
        while (l>=0 && r<s.size() && s[l]==s[r]){
            if (r-l+1 > resLen) {
                resLen = r-l+1;
                res = s.substr(l, r-l+1);
            }
            l--;
            r++;
        }
        //even length palindrome
        l=i,r=i+1;
        while (l>=0 && r<s.size() && s[l]==s[r]){
            if (r-l+1 > resLen) {
                resLen = r-l+1;
                res = s.substr(l, r-l+1);
            }
            l--;
            r++;
        }


    }

    cout <<res <<endl;
}