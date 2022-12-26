import sys

K, N = map(int, input().split())

graph = [int(input()) for _ in range(K)]

lvalue=1
rvalue=max(graph)
value=0

while lvalue <= rvalue:
    value=(rvalue+lvalue)//2
    count = 0
    for i in graph:
        count += i // value
    if count >= N:
        lvalue=value+1
    else:
        rvalue=value-1


sys.stdout.write(str(rvalue))
