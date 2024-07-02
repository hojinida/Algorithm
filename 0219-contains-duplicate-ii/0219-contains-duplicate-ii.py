class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pattern = {}

        for i, num in enumerate(nums):
            if num in pattern and i - pattern[num] <= k:
                return True
            pattern[num] = i