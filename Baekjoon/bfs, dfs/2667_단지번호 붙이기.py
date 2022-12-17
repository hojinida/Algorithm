# dfs 함수
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


# 지도의 크기 입력
n = int(input())

# 지도 자료 입력
arr = [list(map(int, input())) for _ in range(n)]

total = 0
result = []

# 모든 원소를 탐색하며 원소의 값이 1인 경우 total count를 증가시키며 단지 내 집의 수를 result에 저장
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            total += 1
            result.append(dfs(r, c))

# 출력
result.sort()
print(total)
for i in range(total):
    print(result[i])
