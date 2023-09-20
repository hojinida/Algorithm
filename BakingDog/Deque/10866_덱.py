import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):
    data = input().split()

    if data[0] == 'push_back':
        queue.append(data[1])
    elif data[0] == 'push_front':
        queue.appendleft(data[1])
    elif data[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif data[0] == 'size':
        print(len(queue))
    elif queue:
        if data[0] == 'pop_front':
            print(queue.popleft())
        elif data[0] == 'pop_back':
            print(queue.pop())
        elif data[0] == 'front':
            print(queue[0])
        elif data[0] == 'back':
            print(queue[-1])
    else:
        print('-1')
