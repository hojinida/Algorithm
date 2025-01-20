n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(n)]

dp = [[-1] * n for _ in range(n)]
def count_paths(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    if arr[x][y] == 0:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    paths = 0
    step = arr[x][y]

    if x + step < n:
        paths += count_paths(x + step, y)

    if y + step < n:
        paths += count_paths(x, y + step)

    dp[x][y] = paths
    return dp[x][y]


print(count_paths(0, 0))
