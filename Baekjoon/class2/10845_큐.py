import sys
from collections import deque

N = int(input())

q = deque()

arr= [input().split() for _ in range(N)]

for s in arr:

    if s[0] == 'push':
        q.append(int(s[1]))
    elif s[0] == 'front':
        sys.stdout.write('-1' + '\n') if len(q) == 0 else sys.stdout.write(str(q[0]) + '\n')
    elif s[0] == 'back':
        sys.stdout.write('-1' + '\n') if len(q) == 0 else sys.stdout.write(str(q[len(q)-1]) + '\n')
    elif s[0] == 'pop':
        sys.stdout.write('-1' + '\n') if len(q) == 0 else sys.stdout.write(str(q.popleft()) + '\n')
    elif s[0] == 'size':
        sys.stdout.write(str(len(q)) + '\n')
    elif s[0] == 'empty':
        sys.stdout.write('1' + '\n') if len(q) == 0 else sys.stdout.write('0' + '\n')