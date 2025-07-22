#include <iostream>
using namespace std;
#include <string>


int firstOccurence(){
     string haystack="leetcode";
    string needle="eet";

    int n =0;
    int m=0;
    int index=0;

    while(haystack.size()>m){
        if(haystack[m]==needle[n]){
            n++;
            m++;
            if(needle.size()==n){
                
                return m-n;
            }
        }
        else{
            index++;
            m=index;
            n=0;
        }
        

    }
    return -1;
}


int main(){
    cout << firstOccurence() << endl;
    return 0;
   
}