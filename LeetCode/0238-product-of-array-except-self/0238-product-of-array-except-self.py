class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        leftResult = [1 for _ in range(length)]
        rightResult = [1 for _ in range(length)]

        before = 1
        for i in range(length-1):
            leftResult[i] = before*nums[i]
            before = leftResult[i]
        
        before = 1
        for i in range(length-1,0,-1):
            rightResult[i] = before*nums[i]
            before = rightResult[i]
        
        answer = []

        for i in range(length):
            answer.append(leftResult[i-1]*rightResult[(i+1) % length])

        return answer