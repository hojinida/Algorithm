class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def plus(s1,s2):
            return int(s1)+int(s2)
        
        minNum = num1
        maxNum = num2

        if len(num1) > len(num2):
            minNum= num2
            maxNum= num1
        
        pmin = len(minNum)-1
        pmax = len(maxNum)-1

        carry  = 0
        answer = []
        
        while pmin >= 0:
            value = plus(minNum[pmin], maxNum[pmax]) + carry
            carry = value // 10
            answer.append(str(value % 10))
            pmin -= 1
            pmax -= 1

        while pmax >= 0:
            value = int(maxNum[pmax]) + carry
            carry = value // 10
            answer.append(str(value % 10))
            pmax -= 1

        # If there is a carry left
        if carry:
            answer.append(str(carry))

        answer.reverse()
        return "".join(answer)

        