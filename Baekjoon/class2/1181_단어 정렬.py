import sys

N = int(input())

arr = sorted(list(set([input() for _ in range(N)])), key=lambda x: (len(x), x))

for s in arr:
    sys.stdout.write(s + '\n')
