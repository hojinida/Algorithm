import sys
from collections import deque

N = int(input())

graph = [[i for i in input()] for _ in range(N)]

for i in graph:
    q = deque()
    flag=True
    for j in i:
        if j == '(':
            q.append(True)
        elif j == ')':
            if len(q) == 0:
                flag=False
                break
            else:
                q.popleft()
    if len(q)==0 and flag:
        sys.stdout.write('YES'+'\n')
    else:
        sys.stdout.write('NO'+'\n')
