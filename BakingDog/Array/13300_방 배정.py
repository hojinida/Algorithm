x = [0] * 6
y = [0] * 6

n, k = map(int, input().split())

for i in range(n):
    s, g = map(int, input().split())
    if s == 0:
        x[g - 1] += 1
    else:
        y[g - 1] += 1

result = 0

for i in range(6):
    result += ((x[i]-1) // k) + 1
    result += ((y[i]-1) // k) + 1

print(result)