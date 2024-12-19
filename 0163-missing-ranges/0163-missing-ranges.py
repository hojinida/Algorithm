class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        answer = []
        
        for num in nums:
            if num > lower:
                answer.append([lower,num-1])
            
            lower = num+1
        
        if lower <= upper:
            answer.append([lower,upper])

        return answer
            