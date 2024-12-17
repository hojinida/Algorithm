class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        length = 0
        for i in s:
            stack.append(i)
            if len(stack) > 2:
                if stack[-1] == stack[-2] and stack[-2] == stack[-3]:
                    stack.pop()
        
        return "".join(stack)