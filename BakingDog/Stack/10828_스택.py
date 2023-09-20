import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

stack = deque()

for _ in range(n):
    data = input().split()
    if data[0] == 'push':
        stack.append(data[1])
    elif data[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
