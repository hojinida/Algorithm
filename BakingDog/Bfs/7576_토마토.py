import sys
from collections import deque

input = sys.stdin.readline

def bfs(N,M):
    q=deque()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    result =0

    for n in range(N):
        for m in range(M):
            if graph[n][m] == 1:
                q.append(((n,m),0))

    while q:
        (x,y),v = q.popleft()

        for dx,dy in directions:
            nx,ny = x+dx , y+dy
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                q.append(((nx,ny),v+1))
                graph[nx][ny]=1

        result = max(v,result)

    for n in range(N):
        for m in range(M):
            if graph[n][m] == 0:
                return -1
    return result


M, N = map(int, input().split())

graph = [[int(i) for i in input().split()] for _ in range(N)]

print(bfs(N,M))