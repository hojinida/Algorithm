def cul(a,b):
    if a < b:
        temp = a
        a = b
        b = temp
    
    while b != 0 :
        n = a%b
        a=b
        b= n

    return a

class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        answer = 0
        value = 1

        for i in range(1,len(nums)):
            if value is 1:
                answer +=1
                value = cul(nums[i],nums[i-1])
            else:
                value = cul(value,nums[i])

        if value is 1:
            answer+=1

        return answer