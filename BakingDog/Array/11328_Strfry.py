n = int(input())

for i in range(n):
    s1, s2 = input().split()
    print("Possible") if sorted(s1)==sorted(s2) else print("Impossible")