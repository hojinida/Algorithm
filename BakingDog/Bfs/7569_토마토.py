import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

directions = [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]


q = deque()
graph = [[[int(i) for i in input().split()] for _ in range(N)] for _ in range(H)]
visited = set()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                result = -1
                break
            else:
                result=max(result,graph[h][n][m])

print(result)
