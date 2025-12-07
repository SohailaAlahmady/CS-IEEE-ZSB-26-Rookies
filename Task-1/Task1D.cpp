#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int a, b, c, max_val = 0;
        cin >> a >> b >> c;

        max_val = max(a, max(b, c));
        if(max_val == a + b + c - max_val){
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}