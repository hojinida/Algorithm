class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for candidate in candidates:
            for num in range(candidate, target + 1):
                for combination in dp[num - candidate]:
                    dp[num].append(combination + [candidate])
        return dp[target]
                