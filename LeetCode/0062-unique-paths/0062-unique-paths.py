class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 

        for i in range(m):
            for j in range(n):
                up = 0 if i-1 < 0 else dp[i-1][j]
                left = 0 if j-1 < 0 else dp[i][j-1]
                dp[i][j] += up+left
                
        return dp[m - 1][n - 1]


