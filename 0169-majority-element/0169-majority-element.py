class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pattern = {}

        for i in nums:
            if i in pattern:
                pattern[i]+=1
            else:
                pattern[i] = 1

        return max(pattern,key = pattern.get)