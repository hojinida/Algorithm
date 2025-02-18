import re
from itertools import permutations
from collections import deque
def solution(expression):
    expression = re.findall(r'\d+|[+\-*]', expression)
    
    pattern = set()
    for i in expression:
        if i in ["-","*","+"]:
            pattern.add(i)
    pattern = list(permutations(pattern))
    
    def cal(str1,str2,func):
        if func == "+":
            return int(str1) + int(str2)
        elif func == "*":
            return int(str1) * int(str2)
        else:
            return int(str1) - int(str2)

    result = 0
    for pat in pattern:
        exp = deque(expression)
        for i in range(len(pat)):
            q = deque()
            while exp:
                p = exp.popleft()
                if p == pat[i]:
                    q.append(cal(q.pop(),exp.popleft(),p))
                else:
                    q.append(p)
            exp = q
        result = max(result,abs(int(q[0])))
    
    return result
                    
            
        
