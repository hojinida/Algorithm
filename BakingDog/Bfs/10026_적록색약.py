import sys
from collections import deque

input = sys.stdin.readline

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(n, m, c, flag):
    q = deque([(n, m)])
    visited.add((n, m))

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and (graph[nx][ny] == c or (flag and graph[nx][ny] in ['G', 'R'] and graph[x][y] != 'B')) and (
                    nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))


N = int(input())

graph = [[i for i in input().rstrip()] for _ in range(N)]
visited = set()

answer1 = 0

for n in range(N):
    for m in range(N):
        if (n, m) not in visited:
            answer1 += 1
            bfs(n, m, graph[n][m], False)

answer2 = 0
visited = set()

for n in range(N):
    for m in range(N):
        if (n, m) not in visited:
            answer2 += 1
            bfs(n, m, graph[n][m], True)

print(answer1, answer2)
