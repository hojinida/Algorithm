class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)

        pattern = {i for i in nums}

        for i in range(length+1):
            if i not in pattern:
                return i