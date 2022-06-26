from collections import deque
right={'(':0,'{':1,'[':2}
left={')':0,'}':1,']':2}
class Solution:
    def isValid(self, s: str) -> bool:
        temp=deque()
        for i in s:
            if len(temp)==0:
                if i in left:
                    return False
                else:
                    temp.append(i)
            elif i in right:
                temp.append(i)
            elif right[temp[-1]]-left[i]==0:
                temp.pop()
            else:
                return False
        return True if len(temp)==0 else False
        
            