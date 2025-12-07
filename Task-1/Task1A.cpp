#include <iostream>
using namespace std;

int main(){
    int n, ans = 0;
    cin >> n;

    for(int i = 0; i < n; i++){
        int P, V, T;
        cin >> P >> V >> T;
        if (P + V + T >= 2)
            ans++;
    }
    cout << ans << endl;
    return 0;
}