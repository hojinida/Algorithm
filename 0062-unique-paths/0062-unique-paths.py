from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0)) 

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 

        while q:
            x, y = q.popleft()

            if x + 1 < m:
                dp[x + 1][y] += dp[x][y]
                if (x + 1, y) not in visited:
                    q.append((x + 1, y))
                    visited.add((x + 1, y))

            if y + 1 < n:
                dp[x][y + 1] += dp[x][y]
                if (x, y + 1) not in visited:
                    q.append((x, y + 1))
                    visited.add((x, y + 1))

        return dp[m - 1][n - 1]


