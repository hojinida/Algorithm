import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

data = [int(input()) for _ in range(n)]

stack = deque()

answer=n-1
for d in data:
    while stack and stack[-1] <= d:
        stack.pop()
    stack.append(d)
    answer += len(stack)-1
print(answer)


