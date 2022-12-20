import sys
from collections import deque

F, S, G, U, D = map(int, input().split())

dy = [U, -D]
visited = [0 for _ in range(F + 1)]

q = deque()

q.append(S)
visited[S] = 1
while q:
    f = q.popleft()

    for i in range(2):
        df = f + dy[i]
        if 0 < df <= F and visited[df] == 0:
            visited[df] = visited[f] + 1
            q.append(df)

sys.stdout.write("use the stairs") if visited[G] == 0 else sys.stdout.write(str(visited[G] - 1))
