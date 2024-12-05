class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        sortNums = sorted(nums)
        nums += nums
        for i in range(length):
            if nums[i:i+length] == sortNums:
                return True
        
        return False
        
            