import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

data = [int(i) for i in input().split()]

minQ = []
dataQ = deque()
D = []

flag = False
for i in range(n):
    heapq.heappush(minQ, (data[i], i))

    while minQ[0][1] <= i - l:
        heapq.heappop(minQ)

    D.append(minQ[0][0])

for i in range(n):
    print(D[i], end=' ')
print()
