import sys
import heapq

n = int(input())

leftq = []
rightq = []
for i in range(n):
    inputNum = int(sys.stdin.readline())
    if len(leftq) == len(rightq):
        heapq.heappush(leftq, -inputNum)
    else:
        heapq.heappush(rightq, inputNum)
    if rightq and rightq[0] < -leftq[0]:
        leftValue = heapq.heappop(leftq)
        rightValue = heapq.heappop(rightq)

        heapq.heappush(leftq, -rightValue)
        heapq.heappush(rightq, -leftValue)
    print(-leftq[0])
