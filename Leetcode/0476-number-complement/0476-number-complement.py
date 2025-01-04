class Solution:
    def findComplement(self, num: int) -> int:
        answer = []
        
        while num !=0:
            answer.append(num%2)
            num//=2
        
        for i in range(len(answer)):
            if answer[i] == 0:
                answer[i] = 1
            else:
                answer[i] = 0

        result = 0
        for i in range(len(answer)):
            if answer[i] == 1:
                result += 2**i
        
        return result