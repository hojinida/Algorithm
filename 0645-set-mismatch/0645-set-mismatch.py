class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()

        before = 0
        for i in nums:
            if before == i:
                before = i
                break
            before = i
        
        t = sum(nums)
        t2 = sum(i+1 for i in range(len(nums)))

        return [before,before+(t2-t)]
                