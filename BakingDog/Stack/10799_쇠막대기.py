import sys
from collections import deque

input = sys.stdin.readline

s = input()

stack = deque()

answer = 0
flag = True
for i in s:
    if stack and i == ')':
        if flag:
            stack.pop()
            answer += len(stack)
            flag = False
        else:
            stack.pop()
            answer += 1
    else:
        stack.append(i)
        flag = True
print(answer)
