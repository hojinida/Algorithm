class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob_with_dp(houses: List[int]) -> int:
            m = len(houses)
            dp = [0] * m
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, m):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            
            return dp[-1]

        rob_first = rob_with_dp(nums[:-1])
        rob_last = rob_with_dp(nums[1:])

        return max(rob_first, rob_last)