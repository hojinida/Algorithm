import sys
N = int(input())

arr = [int(i) for i in input().split()]

count=0
for i in arr:
    if i != 0 and i != 1:
        flag = True
        for k in range(2, int(i ** 0.5) + 1):
            if i % k == 0:
                flag = False
                break
        if flag: count += 1

sys.stdout.write(str(count))

