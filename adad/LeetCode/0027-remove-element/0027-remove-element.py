class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []

        for i in nums:
            if i != val:
                temp.append(i)
        
        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)