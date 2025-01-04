def cul(n):
        result = 0

        for i in str(n):
            result += int(i)**2
        return result

class Solution:
    def isHappy(self, n: int) -> bool:
        answer = [n]
        while True:
            n = cul(n)
            if n == 1:
                return True
            elif n in answer:
                return False
            answer.append(n)
