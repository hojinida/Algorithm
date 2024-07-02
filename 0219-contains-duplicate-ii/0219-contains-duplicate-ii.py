class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pattern = {}

        for i in range(len(nums)):
            if nums[i] not in pattern:
                pattern[nums[i]] = []
            pattern[nums[i]].append(i)
        

        for key, value in pattern.items():
            length = len(value)
            if length > 1:
                for i in range(length-1):
                    if value[i+1] - value[i] <= k:
                        return True
        
        return False