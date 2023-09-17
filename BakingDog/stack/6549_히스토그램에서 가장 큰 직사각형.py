import sys

input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    n = data[0]
    if n == 0:
        break
    data = data[1:]

    stack = []
    max_area = 0

    for i, h in enumerate(data):
        while stack and data[stack[-1]] > h:
            height = data[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = data[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    print(max_area)

