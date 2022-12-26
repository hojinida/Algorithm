import sys

N = int(input())

A = [int(i) for i in input().split()]
A.sort()

M = int(input())

MA = [int(i) for i in input().split()]

for i in MA:
    rvalue=N-1
    lvalue=0
    flag=False
    while lvalue <= rvalue:
        mid=(rvalue+lvalue)//2
        if A[mid]==i:
            flag=True
            break
        elif A[mid] < i:
            lvalue=mid+1
        else:
            rvalue=mid-1
    if flag: sys.stdout.write('1' + '\n')
    else: sys.stdout.write('0' + '\n')
