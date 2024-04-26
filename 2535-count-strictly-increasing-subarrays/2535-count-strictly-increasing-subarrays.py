class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        preValue = nums[0]
        answer =0 
        temp = 1
        
        for i in nums[1:]:
            if preValue < i :
                temp +=1
            else:
                for j in range(1,temp+1):
                    answer+=j
                temp=1
            preValue = i
    
        for i in range(1,temp+1):
                answer+=i
        
        return answer 