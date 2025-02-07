class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pattern = nums[0]

        if len(nums) ==1:
            return True
            
        dp = [False] * len(nums)
        for index in range(1,len(nums)):
            if index <= pattern:
                pattern = max(pattern,index+nums[index])
                dp[index] = True
        
        return dp[-1]
            
        
        