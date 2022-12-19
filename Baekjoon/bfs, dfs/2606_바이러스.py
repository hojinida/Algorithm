from collections import deque

computerNum = int(input())

n = int(input())

graph = [[] for _ in range(computerNum + 1)]
visit = [False for _ in range(computerNum + 1)]

for _ in range(n):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

q = deque()
q.append(graph[1])
visit[1] = True
count = 0

while q:
    v = q.popleft()
    for i in v:
        if not visit[i]:
            visit[i] = True
            count += 1
            q.append(graph[i])

print(count)
