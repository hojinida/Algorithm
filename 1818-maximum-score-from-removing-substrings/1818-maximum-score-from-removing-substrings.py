class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def deleteS(s,target,plus):
            stack = []
            nonlocal point
            for i in s:
                if stack and stack[-1] == target[0] and i == target[1]:
                    stack.pop()
                    point+=plus
                else:
                    stack.append(i)

            return stack
        point = 0
        result=deleteS(s,"ab",x)
        deleteS("".join(result),"ba",y)
        temp = point

        point = 0
        result=deleteS(s,"ba",y)
        deleteS("".join(result),"ab",x)

        return max(temp,point)