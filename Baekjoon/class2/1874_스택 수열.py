import sys
from collections import deque

N = int(input())

stack = deque([int(input()) for _ in range(N)])


q=deque()

answer=[]

count=1
while stack:
    x = stack.popleft()
    while x not in q:
        q.append(count)
        answer.append('+')
        count+=1
    if q.pop() == x:
        answer.append('-')
    else:
        answer.append('NO')
        break

if 'NO' in answer:
    sys.stdout.write('NO')
else:
    for i in answer:
        sys.stdout.write(str(i)+'\n')

