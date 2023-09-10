import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

stack = deque()
data = deque(int(input()) for _ in range(n))

answer = 0
for d in data:
    while stack and stack[-1] < d:
        stack.pop()
    answer += len(stack)
    stack.append(d)

print(answer)
