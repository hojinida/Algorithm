class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pattern = dict()

        for i, v in enumerate(nums):
            value = target - v
            if value in pattern:
                return [pattern[value],i]
            pattern[v] = i