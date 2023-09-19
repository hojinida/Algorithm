import sys
from collections import deque

input = sys.stdin.readline

n, dn = map(int, input().split())

q = deque(int(i) for i in range(1, n + 1))

data = [int(i) for i in input().split()]

count = 0
for d in data:
    qLen = len(q)
    dw = q.index(d)

    if (qLen - 1) // 2 >= dw and q[0] != d:
        while q and q[0] != d:
            count += 1
            q.append(q.popleft())
    elif q[0] != d:
        while q and q[0] != d:
            count += 1
            q.appendleft(q.pop())
    q.popleft()
print(count)
