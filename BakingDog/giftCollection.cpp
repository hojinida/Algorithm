#include "bits/stdc++.h"
#include <iostream>

using namespace std;
int t, r, c;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
string board[22];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t >> r >> c;
    for (int i = 0; i < r; i++) {
        cin >> board[i];
    }
    stack<tuple<int, int, string>> S;
    int ans = 0;
    S.push({0, 0, {board[0][0]}});
    while (!S.empty()) {
        tuple<int, int, string> cur = S.top(); S.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = get<0>(cur) + dx[dir];
            int ny = get<1>(cur) + dy[dir];
            string ns = get<2>(cur);
            if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
            if (ns.find(board[nx][ny]) != string::npos) continue;
            ns.append({board[nx][ny]});
            ans = max(ans, (int) ns.size());
            S.push({nx, ny, ns});
        }
    }
    cout << ans;
}