class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numSum = 0

        answer = []

        for n in nums:
            numSum+=n
            answer.append(numSum)
        
        return answer