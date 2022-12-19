import sys
from collections import deque

dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

M, N, H = map(int, input().split())

graph = [[[int(i) for i in input().split()] for _ in range(N)] for _ in range(H)]

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and graph[nx][ny][nz]==0:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            queue.append((nx, ny, nz))

answer = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                sys.stdout.write('-1')
                exit(0)
        answer = max(answer,max(j))
sys.stdout.write(str(answer-1))
