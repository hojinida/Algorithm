class Solution:
     def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= mid + 1:
                if mid == len(nums) - 1 or nums[mid + 1] < mid + 1:
                    return mid + 1
                left = mid + 1
            else:
                right = mid
        
        return -1