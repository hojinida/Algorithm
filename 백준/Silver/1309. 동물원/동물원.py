n = int(input())
MOD = 9901

a, b, c = 1, 1, 1 

for _ in range(2, n + 1):
    a, b, c = (a + b + c), (a + c), (a + b)

print((a + b + c) % MOD)