class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        length = len(s)
        for i in range(length):
            if s[i:]+s[0:i] == goal:
                return True
            
        return False
