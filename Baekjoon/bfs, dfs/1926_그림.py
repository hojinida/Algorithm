from collections import deque


def dfs(n, m):
    count = 1
    q = deque()
    q.append((n, m))
    visited[n][m] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            dnx = x + dx[i]
            dny = y + dy[i]
            if 0 <= dnx < N and 0 <= dny < M and visited[dnx][dny] == False and graph[dnx][dny] == 1:
                count += 1
                visited[dnx][dny] = True
                q.append((dnx, dny))
    return count


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())

graph = [[int(i) for i in input().split()] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

answer = []
count = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        if graph[i][j]==1:
            answer.append(dfs(i, j))
            count += 1

print(count)
if answer:
    print(max(answer))
else:
    print(0)
