import sys
from collections import deque

pattern = {'(': ')', '[': ']'}

input = sys.stdin.readline

s = input().rstrip()

stack = deque()

S = 0
B = 0

answer = 0
flag = False
for i in s:
    if stack and pattern.get(stack[-1]) == i:
        p = stack.pop()
        if p == '[':
            B -= 1
        else:
            S -= 1
        if not flag:
            mul = 1
            if B != 0: mul *= (3 ** B)
            if S != 0: mul *= (2 ** S)
            if p == '[':
                answer += (3 * mul)
            else:
                answer += (2 * mul)
            flag = True
    else:
        stack.append(i)
        if i == '[':
            B += 1
        else:
            S += 1
        flag = False

print(answer) if not stack else print(0)
