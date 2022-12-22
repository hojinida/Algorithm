N = int(input())

T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

d=[0]*(N+1)
for i in range(N-1,-1,-1):
    if N<i+T[i]:
        d[i]=d[i+1]
    else:
        d[i]=max(d[i+1],P[i]+d[i+T[i]])

print(d[0])