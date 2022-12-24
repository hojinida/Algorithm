import sys
from collections import deque


def dfs(d, n, m, cul, t):
    if d == 4:
        result.append(cul)
        return
    if n - 1 >= 0 and t != 1:
        dfs(d + 1, n - 1, m, cul + arr[n][m], 0)
    if n + 1 < r and t != 0:
        dfs(d + 1, n + 1, m, cul + arr[n][m], 1)
    if m - 1 >= 0 and t != 3:
        dfs(d + 1, n, m - 1, cul + arr[n][m], 2)
    if m + 1 < c and t != 2:
        dfs(d + 1, n, m + 1, cul + arr[n][m], 3)
    return


def pattern(n, m):
    if n - 1 >= 0 and m - 1 >= 0 and m + 1 < c:
        result.append(arr[n][m] + arr[n - 1][m] + arr[n][m - 1] + arr[n][m + 1])
    if n + 1 < r and m - 1 >= 0 and m + 1 < c:
        result.append(arr[n][m] + arr[n + 1][m] + arr[n][m - 1] + arr[n][m + 1])
    if n - 1 >= 0 and n + 1 < r and m + 1 < c:
        result.append(arr[n][m] + arr[n + 1][m] + arr[n - 1][m] + arr[n][m + 1])
    if n - 1 >= 0 and n + 1 < r and m - 1 >= 0:
        result.append(arr[n][m] + arr[n + 1][m] + arr[n - 1][m] + arr[n][m - 1])
    return


r, c = map(int, input().split())
arr = [[i for i in map(int, input().split())] for _ in range(r)]

result = deque()
for i in range(r):
    for j in range(c):
        dfs(0, i, j, 0, 4)
        pattern(i, j)
sys.stdout.write(str(max(result)))