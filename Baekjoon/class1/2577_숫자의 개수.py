import sys

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul = str(mul)
for i in range(10):
    sys.stdout.write(str(mul.count(str(i)))+'\n')
