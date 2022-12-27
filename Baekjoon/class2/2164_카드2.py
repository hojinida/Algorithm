import sys
from collections import deque

N = int(input())

q = deque(int(i) for i in range(1, N + 1))

while len(q)!=1:
    q.popleft()
    q.append(q.popleft())

sys.stdout.write(str(q.popleft()))
