import sys
import ast
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    order = input()
    i = int(input())
    data = deque(ast.literal_eval(input()))

    order_reverse = False
    error_occurred = False
    for o in order:
        if o == 'R':
            order_reverse = not order_reverse
        elif o == 'D':
            if not data:
                print('error')
                error_occurred = True
                break
            if order_reverse:
                data.pop()
            else:
                data.popleft()
    if error_occurred:
        continue
    if order_reverse:
        data.reverse()
    print('[' + ','.join(map(str, data)) + ']')
