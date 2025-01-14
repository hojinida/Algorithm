n,m = map(int,input().split())

miro = [[int(i) for i in input().split()] for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = miro[0][0]

for r in range(n):
    for c in range(m):
        if r > 0:
            dp[r][c] = max(dp[r][c],dp[r-1][c]+miro[r][c])
        if c > 0:
            dp[r][c] = max(dp[r][c],dp[r][c-1]+miro[r][c])
        if r > 0 and c > 0:
            dp[r][c] = max(dp[r][c],dp[r-1][c-1]+miro[r][c])

print(dp[n-1][m-1])