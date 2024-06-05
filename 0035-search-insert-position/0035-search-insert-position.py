class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        answer = 0

        while start < end :
            index = (start + end) // 2
            if nums[index] > target:
                end = index -1 
            elif nums[index] < target:
                start = index + 1
            else:
                return index
        if nums[start] >= target:
            return start
        else:
            return start+1
    