import sys
from collections import deque

input = sys.stdin.readline

def bfs(N,M):
    q=deque()
    fq=deque()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    fc=1

    for n in range(N):
        for m in range(M):
            if graph[n][m] == 'J':
                q.append(((n,m),1))
                visited.add((n,m))
            elif graph[n][m] == 'F':
                fq.append(((n,m),1))

    while q:
        (x,y),v = q.popleft()

        if x==0 or x==N-1 or y==0 or y==M-1:
            return v

        while fq and fc == v:
            (fx, fy),fv = fq.popleft()
            if fv > v:
                fq.append(((fx, fy),fv))
                fc+=1
                break
            for dx, dy in directions:
                nx, ny = fx + dx, fy + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != '#' and graph[nx][ny] != 'F':
                    fq.append(((nx, ny),fv+1))
                    graph[nx][ny] = 'F'


        for dx,dy in directions:
            nx,ny = x+dx , y+dy
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == '.' and (nx,ny) not in visited:
                q.append(((nx,ny),v+1))
                visited.add((nx,ny))

    return 'IMPOSSIBLE'

N, M = map(int, input().split())

graph = [[i for i in input().rstrip()] for _ in range(N)]

print(bfs(N,M))


