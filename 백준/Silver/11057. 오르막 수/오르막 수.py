n = int(input())

dp = [[1]*10 for _ in range(n)]

for i in range(1,n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1]) - sum(dp[i-1][0:j])

print(sum(dp[-1])%10007)