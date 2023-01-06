import sys

N = int(input())

q = [int(i) for i in input().split()]

for i in range(1, N):
    q[i] = max(q[i], q[i-1]+q[i])

sys.stdout.write(str(max(q)))
