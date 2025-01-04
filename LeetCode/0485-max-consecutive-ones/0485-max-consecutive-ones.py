class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        temp = 0
        for n in nums:
            if n == 1:
                temp+=1
            else:
                answer = max(answer,temp)
                temp=0
        
        answer = max(answer,temp)

        return answer