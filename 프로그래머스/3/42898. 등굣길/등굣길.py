def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] =1
    
    water = set()
    for p in puddles:
        water.add(tuple(p))
    
    for i in range(n):
        for j in range(m):
            if (j+1,i+1) in water:
                continue
            if i-1 >= 0:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 0:
                dp[i][j] += dp[i][j-1]
                
    return dp[n-1][m-1] % 1000000007