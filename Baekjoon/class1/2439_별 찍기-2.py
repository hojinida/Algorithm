import sys

N = int(input())

for i in range(N-1,-1,-1):
    for j in range(N):
        if j<i:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('*')
    sys.stdout.write('\n')