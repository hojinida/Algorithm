import sys
from collections import deque

input = sys.stdin.readline

def bfs(a,k):
    q = deque([(a,0)])

    visited =set()

    while q:
        c,operations = q.popleft()

        if c == k:
            return operations

        if c in visited:
            continue

        visited.add(c)

        if c < k:
            q.append((c*2,operations+1))
            q.append((c+1,operations+1))

a,k = map(int,input().split())

print(bfs(a,k))







