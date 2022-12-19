import sys
from collections import deque
n = int(input())

x, y = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

q=deque()
q.append(y)
visit[y]=1

while q:
    v=q.popleft()
    for i in graph[v]:
        if visit[i]==0:
            visit[i] = (visit[v]+1)
            q.append(i)

if visit[x] > 0:
    sys.stdout.write(str(visit[x]-1))
else:
    sys.stdout.write('-1')
