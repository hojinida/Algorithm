from collections import deque
import sys

input = sys.stdin.readline

s = deque(input().strip())

left_stack = deque()
right_stack = s

n = int(input().strip())

for _ in range(n):
    data = input().strip()
    if data[0] == 'P':
        right_stack.append(data[2])
    elif data == 'L':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif data == 'D':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif data == 'B':
        if right_stack:
            right_stack.pop()

print(''.join(right_stack) + ''.join(left_stack)[::-1])

