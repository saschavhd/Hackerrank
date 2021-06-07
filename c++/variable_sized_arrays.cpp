#include <vector>
#include <iostream>
using namespace std;


int main() {
    int n, q, size, value, row, column;
    cin >> n >> q;
    vector<vector<int>> big_vec;
    for (int i = 0; i < n; i++) {
        cin >> size;
        vector<int> small_vec;
        for (int j = 0; j < size; j++) {
            cin >> value;
            small_vec.push_back(value);
        }
        big_vec.push_back(small_vec);
    }
    for (int k = 0; k < q; k++) {
        cin >> row >> column;
        cout << big_vec[row][column] << endl;
    }
    return 0;
}
