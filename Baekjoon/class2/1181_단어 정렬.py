import sys

N = int(input())

arr=[input() for _ in range(N)]

arr=set(arr)
arr=list(arr)
arr.sort(key=lambda x:(len(x),x))

for s in arr:
    sys.stdout.write(s+'\n')