import sys
from collections import deque

input = sys.stdin.readline


def bfs(N, M):
    q = deque([((0, 0), 1)])
    visited = {0, 0}

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while q:
        (x, y), v = q.popleft()

        if x == N - 1 and y == M - 1:
            return v

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), v + 1))

    return -1


N, M = map(int, input().split())

graph = [[int(i) for i in input().rstrip()] for _ in range(N)]

print(bfs(N,M))

