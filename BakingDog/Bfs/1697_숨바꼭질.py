import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([(N, 0)])
visited = {N}

operations = [
    lambda x: x - 1,
    lambda x: x + 1,
    lambda x: x * 2
]
answer = 0

while q:
    (n, v) = q.popleft()

    if n == K:
        answer = v
        break

    for operation in operations:
        o = operation(n)
        if 0 <= o <= 100000 and o not in visited:
            visited.add(o)
            q.append((o, v + 1))

print(answer)
