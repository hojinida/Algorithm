class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        ig = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(["(",i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    ig.append(i)
        for i in stack:
            ig.append(i[1])
        
        answer = []
        for i in range(len(s)):
            if i not in ig:
                answer.append(s[i])
        
        return "".join(answer)
            