class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        maxValue = float('-inf')
        
        maxValue = max(maxValue,(nums[-1]*nums[-2]*nums[-3]))
        maxValue = max(maxValue,(nums[0]*nums[1]*nums[-1]))

        return maxValue