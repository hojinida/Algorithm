class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        index = 0
        last = ""
        for i in nums:
            if last != i:
                nums[index] = i
                index+=1
            last=i
        
        return index