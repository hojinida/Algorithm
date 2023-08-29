from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = deque(input().strip())
    rightStack = deque()
    leftStack = deque()

    for j in s:
        if j == '<':
            if len(rightStack) != 0:
                leftStack.append(rightStack.pop())
        elif j == '>':
            if len(leftStack) != 0:
                rightStack.append(leftStack.pop())
        elif j == '-':
            if len(rightStack) != 0:
                rightStack.pop()
        else:
            rightStack.append(j)
    leftStack.reverse()
    print(''.join(rightStack) + ''.join(leftStack))
