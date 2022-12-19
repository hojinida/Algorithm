n, k = map(int, input().split())

knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
arr=[[0,0]]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n+1):
    for j in range(k+1):
        w=arr[i][0]
        v=arr[i][1]
        if j < w:
            knapsack[i][j]=knapsack[i-1][j]
        else:
            knapsack[i][j]=max(v + knapsack[i - 1][j - w],knapsack[i-1][j])
print(knapsack[n][k])
