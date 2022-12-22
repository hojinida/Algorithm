import sys

n = int(input())

for i in range(n):
    r, s = input().split()
    for j in range(len(s)):
        for _ in range(int(r)):
            sys.stdout.write(s[j])
    sys.stdout.write('\n')
