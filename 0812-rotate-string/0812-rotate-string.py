from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = deque(s)

        for _ in range(len(s)):
            if "".join(s) == goal:
                return True
            s.append(s.popleft())
            
        return False
