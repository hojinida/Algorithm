class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pattern = {}

        for i in nums:
            if i in pattern:
                pattern[i]+=1
            else:
                pattern[i] = 1

        n = len(nums) // 2
        for key,value in pattern.items():
            if value > n:
                return key
        return 0