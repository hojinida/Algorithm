stairs = [int(input()) for _ in range(int(input()))]

if len(stairs) == 1:
    print(stairs[0])
elif len(stairs) == 2:
    print(stairs[0] + stairs[1])
else:
    dp = [0] * (len(stairs))
    dp[0] = stairs[0]
    dp[1] = stairs[1] + dp[0]
    dp[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])

    for i in range(3, len(stairs)):
        dp[i] = max(stairs[i - 1] + dp[i - 3] + stairs[i], dp[i - 2] + stairs[i])

    print(dp[-1])