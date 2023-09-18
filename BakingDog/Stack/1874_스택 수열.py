import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

data = [int(input()) for _ in range(n)]

leftStack = deque(range(n, 0, -1))
rightStack = deque()

result = []
flag = True
for i in data:
    while i not in rightStack and len(leftStack) != 0:
        rightStack.append(leftStack.pop())
        result.append('+')
    if len(rightStack) != 0 and rightStack.pop() == i:
        result.append('-')
    else:
        flag = False
        break

if flag:
    for i in result:
        print(i)
else:
    print('NO')
