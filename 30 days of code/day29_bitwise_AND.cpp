#include <bits/stdc++.h>

using namespace std;

void solve() {
    int t;
    cin >> t;
    for (int itr = 0; itr < t; itr++) {
        int n; int k; int m = 0;
        cin >> n >> k;
        for (int i = 1; i < n; i++) {
            for (int = i+1; j <= n; j++) {
                if ((i & j) > m && (i & j) < k) {
                    m = (i & j);
                }
            }
        }
        cout << m << endl;
    }
}
