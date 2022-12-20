import sys
from collections import deque


def check():
    ice = deque()
    zero= deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                zero.append((i, j))
            else:
                ice.append((i,j))
    return ice,zero



def m_bfs(x,y):
    visited[x][y]=True
    for i in range(4):
        dn = x + dx[i]
        dm = y + dy[i]
        if 0 <= dn < N and 0 <= dm < M and graph[dn][dm] == 0 and visited[dn][dm] == False and graph[x][y] != 0:
            graph[x][y] -= 1


def check_bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        n, m = q.popleft()
        for i in range(4):
            dn = n + dx[i]
            dm = m + dy[i]
            if 0 <= dn < N and 0 <= dm < M and visited[dn][dm] == False and graph[dn][dm] > 0:
                visited[dn][dm] = True
                q.append((dn, dm))
    return True


N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[int(i) for i in input().split()] for _ in range(N)]

answer = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    count=0
    flag=False
    for i in range(1,N-1):
        for j in range(1,M-1):
            if graph[i][j]!=0 and visited[i][j] == False:
                flag=True
                if check_bfs(i,j) : count+=1
    if not flag :
        answer=0
        break
    if count > 1 : break
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if graph[i][j]!=0 :
                m_bfs(i,j)
    answer += 1

sys.stdout.write(str(answer))
