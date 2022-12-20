import sys
from collections import deque

n, k = map(int, input().split())

dx = [1, -1, 0]
visited = {}

q = deque()

q.append(n)
visited[n] = 1

while q:
    x = q.popleft()

    for i in range(3):
        dnx = x + dx[i] if i < 2 else x * 2
        if 0 <= dnx < 100001 and visited.get(dnx) is None:
            visited[dnx] = visited.get(x) + 1
            q.append(dnx)
    if visited.get(k) is not None:
        break

print(visited.get(k) - 1)
