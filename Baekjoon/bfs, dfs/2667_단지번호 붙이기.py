def dfs(r, c):
    if arr[r][c] == 1:
        arr[r][c] = 0
        count = 1
        if r > 0:
            count += dfs(r - 1, c)
        if r < n - 1:
            count += dfs(r + 1, c)
        if c > 0:
            count += dfs(r, c - 1)
        if c < n - 1:
            count += dfs(r, c + 1)
        return count
    return 0


n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

total = 0
result = []

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            total += 1
            result.append(dfs(r, c))

result.sort()
print(total)
for i in range(total):
    print(result[i])
