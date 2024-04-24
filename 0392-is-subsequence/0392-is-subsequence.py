from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = deque(t)
        s = deque(s)
        
        while q and s:
            p = q.popleft()

            if p == s[0] :
                s.popleft()

        return True if len(s) == 0 else False
        