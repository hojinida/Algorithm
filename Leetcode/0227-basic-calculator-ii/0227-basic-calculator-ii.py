from collections import deque
import re
class Solution:
    def calculate(self, s: str) -> int:
        s = re.findall(r'\d+|[+*/-]', s)
        
        q = deque(s)
    
        answer = deque()
        while q:
            p = q.popleft()
            if p == "*":
                answer.append(int(answer.pop()) * int(q.popleft()))
            elif p == "/":
                answer.append(int(answer.pop()) // int(q.popleft()))
            else:
                answer.append(p)
      
        result = int(answer.popleft())
        while answer:
            p = answer.popleft()
            if p == "+":
                result += int(answer.popleft())
            elif p == "-":
                result -= int(answer.popleft())
        
        return result


                