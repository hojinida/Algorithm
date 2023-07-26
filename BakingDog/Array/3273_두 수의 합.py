N = int(input())

A = [int(i) for i in input().split()]

target = int(input())

A.sort()

result = 0
start = 0
end = len(A) - 1

while start < end:
    if A[start] + A[end] == target:
        result += 1
        start += 1
        end -= 1
    elif A[start] + A[end] < target:
        start += 1
    else:
        end -= 1

print(result)
