import sys
from collections import deque

testCase = int(input())

for _ in range(testCase):
    N, M = map(int, input().split())
    q = deque((int(i), False) if index != M else (int(i), True) for index, i in enumerate(input().split()))

    count=1
    while q:
        flag=True
        x=q.popleft()
        for k in q:
            if x[0] < k[0]:
                q.append(x)
                flag=False
                break
        if flag and x[1]:
            sys.stdout.write(str(count)+'\n')
        if flag: count+=1