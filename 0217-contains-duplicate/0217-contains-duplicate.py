class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pattern={}

        for i in nums:
            if i in pattern:
                return True
            else:
                pattern[i] = 0
        
        return False