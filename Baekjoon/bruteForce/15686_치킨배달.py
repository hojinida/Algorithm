import sys
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
arr = [[int(i) for i in input().split()] for _ in range(n)]

home = deque()
dak = deque()
for row in range(n):
    for colum in range(n):
        if arr[row][colum] == 1:
            home.append((row, colum))
        elif arr[row][colum] == 2:
            dak.append((row, colum))
pattern = list(combinations(dak, m))
result=[]
for i in pattern:
    temp=0
    for h in home:
        t=100
        for k in i:
            t=min((abs(k[0]-h[0])+abs(k[1]-h[1])),t)
        temp+=t
    result.append(temp)
sys.stdout.write(str(min(result)))