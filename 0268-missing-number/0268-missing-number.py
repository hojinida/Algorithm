from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pattern = {i for i in nums}

        for i in range(len(nums)+1):
            if i not in pattern:
                return i
        
        