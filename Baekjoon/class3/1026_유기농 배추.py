import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
num = int(input())


def bfs(n, m):
    q = deque()
    q.append((n, m))
    visited[n][m] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            dnx = x + dx[i]
            dny = y + dy[i]
            if 0 <= dnx < N and 0 <= dny < M and visited[dnx][dny] == False and graph[dnx][dny] == 1:
                q.append((dnx, dny))
                visited[dnx][dny] = True


for _ in range(num):
    N, M, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    arr = [input().split() for _ in range(K)]

    for x, y in arr:
        graph[int(x)][int(y)] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == False:
                count += 1
                bfs(i, j)
    sys.stdout.write(str(count) + '\n')
