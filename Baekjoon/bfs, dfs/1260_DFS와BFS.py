from collections import deque


def dfs(key):
    print(key, end=" ")
    visit.append(key)
    if dic.get(key) is not None:
        for i in dic.get(key):
            if i not in visit:
                dfs(i)


def bfs(key):
    q = deque()
    q.append(key)
    visit.append(key)

    while q:
        v = q.popleft()
        print(v, end=" ")
        if dic.get(v) is not None:
            for i in dic.get(v):
                if i not in visit:
                    q.append(i)
                    visit.append(i)


# 정점,간선의 개수 시작 정점 입력
v, e, v_num = map(int, input().split())

# 딕셔너리에 각 정점에 대한 간선 저장
dic = {}

for i in range(e):
    v1, v2 = map(int, input().split())
    if v1 not in dic:
        dic[v1] = [v2]
    else:
        dic.get(v1).append(v2)
    if v2 not in dic:
        dic[v2] = [v1]
    else:
        dic.get(v2).append(v1)

# 정렬
for i in dic.keys():
    dic.get(i).sort()

# 출력
visit = []
dfs(v_num)
print()
visit.clear()
bfs(v_num)
