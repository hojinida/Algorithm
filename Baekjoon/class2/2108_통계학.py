import sys
from collections import Counter

N = int(input())

arr = sorted([int(input()) for _ in range(N)])
cnt = Counter(arr)
cnt = sorted(list(cnt.most_common()),key=lambda x: -x[1])

sys.stdout.write(str(round(sum(arr)/N)) + '\n')
sys.stdout.write(str(arr[N // 2]) + '\n')
sys.stdout.write(str(cnt[1][0]) + '\n') if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else sys.stdout.write(str(cnt[0][0]) + '\n')
sys.stdout.write(str(arr[N - 1] - arr[0])) if N > 1 else sys.stdout.write(str('0'))
