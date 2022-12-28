import sys

N = int(input())

for i in range(N // 5, -1, -1):
    if N - (5 * i) == 0 or (N - (5 * i)) % 3 == 0:
        sys.stdout.write(str(i + (N - (i * 5)) // 3))
        exit(0)
sys.stdout.write('-1')
