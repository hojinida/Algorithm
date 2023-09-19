import sys
from collections import deque

input = sys.stdin.readline

data = deque(i for i in range(int(input()), 0, -1))

while len(data) > 1:
    data.pop()
    data.appendleft(data.pop())

print(data.pop())