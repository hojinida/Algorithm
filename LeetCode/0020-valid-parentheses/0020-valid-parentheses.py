class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {"(":")","{":"}","[":"]"}
        stack = []

        for char in s:
            if char in pattern:
                stack.append(char)
            else:
                if not stack or pattern[stack.pop()] != char:
                    return False
        
        return not stack