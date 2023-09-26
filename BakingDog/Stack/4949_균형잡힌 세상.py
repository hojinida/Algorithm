import sys
from collections import deque

input = sys.stdin.readline

pattern = {']': '[', ')': '('}

while 1:
    data = input()
    stack = deque()

    flag = True
    if data[0] == '.':
        break
    for d in data:
        if d == '(' or d == '[':
            stack.append(d)
        elif d == ')' or d == ']':
            if not stack or stack.pop() != pattern[d]:
                flag = False
                break
    if stack:
        flag = False
    print("yes") if flag else print("no")
