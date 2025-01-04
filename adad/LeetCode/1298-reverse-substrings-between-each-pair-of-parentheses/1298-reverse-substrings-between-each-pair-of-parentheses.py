class Solution:
    def reverseParentheses(self, s: str) -> str:
        index = 0
        def order():
            nonlocal index
            stack = []
            while index < len(s):
                if s[index] == "(":
                    index+=1
                    stack+=order()
                elif s[index] == ")":
                    return list(reversed(stack))
                else:
                    stack.append(s[index])
                index+=1
                
            return stack

        return "".join(order())

        
                
                