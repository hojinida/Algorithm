n = int(input())
arr = [int(i) for i in input().split()]

dp = [0] * n  
dp[0] = 1 

for i in range(1, n):
    dp[i] = 1
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) 