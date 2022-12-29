import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        start = q.popleft()

        for k in graph[start]:
            if visited[k] == 0:
                visited[k] += visited[start] + 1
                q.append(k)


N, M = map(int, input().split())

graph = [[] for _ in range(M + 2)]

for _ in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

answer = []
for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    bfs(i)
    answer.append(sum(visited) - 1)

sys.stdout.write(str(answer.index(min(answer)) + 1))
