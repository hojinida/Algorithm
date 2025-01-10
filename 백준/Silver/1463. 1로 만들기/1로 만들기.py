from collections import deque
input = int(input())

q = deque()
pattern  = {}
q.append((input,0))

while q:
    p,count = q.popleft()
    if p in pattern:
        continue
    pattern[p] = 0
    if p == 1:
        print(count)
        break
    if p % 3 == 0:
        q.append((p//3,count+1))
    if p %2 == 0:
        q.append((p//2, count + 1))
    q.append((p -1, count + 1))

