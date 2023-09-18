import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = deque(map(int, input().split()))

stack = deque()
answer = []
for index, d in enumerate(data):
    while stack and stack[-1][0] < d:
        stack.pop()
    if not stack:
        answer.append("0 ")
    else:
        answer.append(str(stack[-1][1])+" ")
    stack.append([d, index + 1])

print(''.join(answer))

