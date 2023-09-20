import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

data = [int(i) for i in input().split()]

data.reverse()

stack = deque()
answer = []

for d in data:
    while stack and stack[-1] <= d:
        stack.pop()
    if stack:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(d)

answer.reverse()

for i in answer:
    print(i, end=' ')
