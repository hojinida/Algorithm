import sys

N = int(input())

for i in range(N):
    n = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    for k in range(2, n + 1):
        zero.append(zero[k - 1] + zero[k])
        one.append(one[k - 1] + one[k])
    sys.stdout.write(str(zero[n]) + " " + str(one[n]) + '\n')
