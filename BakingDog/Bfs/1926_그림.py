import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j):
    result = 1
    q = deque()
    q.append((i, j))
    graph[i][j] = True

    while q:
        i, j = q.popleft()
        for dn, dm in pattern:
            ni, nj = i + dn, j + dm
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and not graph[ni][nj]:
                q.append((ni, nj))
                graph[ni][nj] = True
                result += 1
    return result

pattern = [(0, 1), (0, -1), (1, 0), (-1, 0)]

pc = 0  # 칠해진 구성 요소 수
mb = 0  # 최대 블록 크기

n, m = map(int, input().split())
arr = [[int(i) for i in input().split()] for _ in range(n)]
graph = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not graph[i][j]:
            pc += 1
            mb = max(mb, bfs(i, j))

print(pc)
print(mb)

