from collections import deque

M, N = map(int, input().split())

visited = [[False for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(one):
    q = one

    while q:
        n, m = q.popleft()
        visited[n][m] = True

        for i in range(4):
            dn = n + dx[i]
            dm = m + dy[i]
            if 0 <= dn < N and 0 <= dm < M and visited[dn][dm] == False and graph[dn][dm] == 0:
                graph[dn][dm] = graph[n][m] + 1
                visited[dn][dm] = True
                q.append((dn, dm))


graph = [[int(i) for i in input().split()] for _ in range(N)]

checkOne = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            checkOne.append((i, j))
bfs(checkOne)

flag=True
maxV=0
for i in range(N):
    if 0 in graph[i]:
        flag=False
    else:
        maxV=max(maxV,max(graph[i]))

if flag:
    print(maxV-1)
else:
    print(-1)