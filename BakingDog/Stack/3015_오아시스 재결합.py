import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

data = [int(input()) for _ in range(n)]

stack = deque()

answer = 0
for d in data:
    while stack and stack[-1][0] < d:
        answer += stack.pop()[1] + 1
    if stack and stack[-1][0] == d:
        stack.append([d, stack[-1][1] + 1])
    elif stack and stack[-1][0] > d:
        stack.append([d, 1])
    else:
        stack.append([d, 0])
for s, i in stack:
    answer += i

print(answer)
