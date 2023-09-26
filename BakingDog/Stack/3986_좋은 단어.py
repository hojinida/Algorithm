import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n):
    data = deque(d for d in input() if d != '\n')
    stack = deque()
    flag = True
    while data:
        pop = data.popleft()
        if stack and stack[-1] == pop:
            stack.pop()
        else:
            stack.append(pop)
    if not stack:
        answer += 1

print(answer)
