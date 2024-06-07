from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = deque(a)
        b = deque(b)
       
        answer = []
        plus = 0
        while a or b:
            ap = 0
            bp = 0
            if a :
                ap = int(a.pop())
            if b :
                bp = int(b.pop())
            s = ap + bp + plus
            if s > 1:
                plus=1
                s%=2
            else:
                plus = 0
            answer.append(s)
        if plus == 1:
            answer.append(1)
        answer.reverse()

        answer = "".join(map(str,answer))

        return answer