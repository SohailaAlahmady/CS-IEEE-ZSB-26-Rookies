#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    
    string cf = "codeforces";
    for(int i = 1; i <= n; ++i){
        char c ;
        cin >> c;
        if(cf.find(c) != string::npos){
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}