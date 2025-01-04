class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[point]
                nums[point] = nums[i]
                nums[i] = temp
                point+=1
        
        