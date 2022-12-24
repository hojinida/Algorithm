import copy

start = ['W', 'B']

pattern = {'W': 'B', 'B': 'W'}

N, M = map(int, input().split())

graph = [[i for i in input()] for _ in range(N)]


answer = []
for p in start:
    values = [[0 for _ in range(M)] for _ in range(N)]
    columBefore = ''
    lowBefore = ''
    temp = copy.deepcopy(graph)
    temp[0][0]=p
    for i in range(N):
        if temp[i][0] == lowBefore:
            values[i][0] = 1
            temp[i][0] = pattern[temp[i][0]]
        for j in range(1,M):
            if temp[i][j] == columBefore:
                temp[i][j] = pattern[temp[i][j]]
                values[i][j] = 1
            columBefore = temp[i][j]
        lowBefore = temp[i][0]
    for k in range(0,N-7):
        for i in values[k:k+8]:
            print(i)
