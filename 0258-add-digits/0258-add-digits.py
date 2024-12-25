class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            answer = 0
            for i in str(num):
                answer+=int(i)
            num = answer
        
        return num