def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]

    return dp[n]

count = int(input())
for _ in range(count):
    target = int(input())
    print(count_ways(target))