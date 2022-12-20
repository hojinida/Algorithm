import sys
from collections import deque


def check(num):
    temp = list()
    for i in range(N):
        for j in range(N):
            if num <= graph[i][j]:
                temp.append((i, j))
    return temp


def bfs(num, x, y):
    flag = False
    q = deque()
    q.append((x, y))
    if visited[x][y] == 0:
        flag = True
    visited[x][y] = 1
    while q:
        n, m = q.popleft()
        for i in range(4):
            dn = n + dx[i]
            dm = m + dy[i]
            if 0 <= dn < N and 0 <= dm < N and graph[dn][dm] >= num and visited[dn][dm] == 0:
                visited[dn][dm] = 1
                q.append((dn, dm))
    return flag


N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[int(i) for i in input().split()] for _ in range(N)]

answer = 0
for i in range(1, 101):
    temp = check(i)
    count = 0
    if len(temp) == 0: break
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x, y in temp:
        if bfs(i, x, y):
            count += 1
    answer = max(answer, count)

sys.stdout.write(str(answer))
