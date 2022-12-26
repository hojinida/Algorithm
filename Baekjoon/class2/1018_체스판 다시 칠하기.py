import copy
import sys

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
    if temp[0][0] != p:
        temp[0][0] = p
        values[0][0] = 1
    columBefore=p
    for i in range(N):
        if temp[i][0] == lowBefore:
            values[i][0] = 1
            temp[i][0] = pattern[temp[i][0]]
        columBefore=temp[i][0]
        for j in range(1, M):
            if temp[i][j] == columBefore:
                temp[i][j] = pattern[temp[i][j]]
                values[i][j] = 1
            columBefore = temp[i][j]
        lowBefore = temp[i][0]
    for i in range(N - 7):
        for j in range(M - 7):
            count = 0
            for s in [row[j:j + 8] for row in values[i:i + 8]]:
                count += s.count(1)
            answer.append(count)

sys.stdout.write(str(min(answer)))
