import sys
from collections import deque

input = sys.stdin.readline

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    cq = deque([])
    visited = set()
    answer = 0
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1
        cq.append((n, m))

    for n, m in cq:
        if (n, m) not in visited:
            q = deque([(n, m)])
            visited.add((n, m))

            while q:
                (x, y) = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            answer += 1

    print(answer)
