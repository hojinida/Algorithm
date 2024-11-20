class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        value = n * (n+1) // 2
        
        return value - sum(nums)
        
        
        