import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

right_stack = deque(range(n,0,-1))
left_stack= deque()

print('<',end='')

for i in range(n):
    for j in range(k):
        if len(right_stack) == 0:
            left_stack.reverse()
            right_stack = deque.copy(left_stack)
            left_stack.clear()
        left_stack.append(right_stack.pop())
    print(left_stack.pop(),end=', ') if i != n-1 else print(left_stack.pop(),end='>')
