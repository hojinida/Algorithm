import sys
from collections import deque

input = sys.stdin.readline


def dfs(a, k, memo=None):
    if memo is None:
        memo = {}

    if a == k:
        return 0

    if a > k:
        return float('inf')

    if a in memo:
        return memo[a]

    op1 = dfs(a + 1, k, memo)

    op2 = dfs(a * 2, k, memo)

    memo[a] = 1 + min(op1, op2)
    return memo[a]


a, k = map(int, input().split())
print(dfs(a, k))
