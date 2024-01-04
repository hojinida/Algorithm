import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, m):
    q = deque([((0, 0), 0)])
    visited = {(0, 0)}

    directions = [(0, 1), (1, 0)]

    while q:
        (x, y), cv = q.popleft()

        if x == n - 1 and y == m - 1:
            return cv

        boost = graph[x][y]

        for dx, dy in directions:
            for s in range(1, boost + 1):
                nx, ny = x + dx * s, y + dy * s

                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append(((nx, ny), cv + 1))
    return -1


n, m = map(int, input().split())

graph = [[int(i) for i in input().split()] for _ in range(n)]

print(bfs(n,m))