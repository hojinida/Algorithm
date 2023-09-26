import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    data = deque(d for d in input() if d != '\n')
    stack = deque()
    flag = True
    while data:
        pop = data.popleft()
        if pop == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
        else:
            stack.append(pop)
    if stack:
        flag = False
    print("YES") if flag else print("NO")
