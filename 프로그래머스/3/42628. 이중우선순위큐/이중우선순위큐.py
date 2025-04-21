import heapq
from collections import Counter
def solution(operations):
    maxQ = []
    minQ = []
    count = Counter()
    
    for o in operations:
        oper, value = o.split()
        value = int(value)

        if oper == "I":
            count[value] += 1
            heapq.heappush(maxQ, -value)
            heapq.heappush(minQ, value)
        elif oper == "D" and value ==  1:
            while maxQ and count[-maxQ[0]] == 0:
                heapq.heappop(maxQ)
            if maxQ:
                x = -heapq.heappop(maxQ)
                count[x] -= 1
        elif oper == "D" and value == -1:
            while minQ and count[minQ[0]] == 0:
                heapq.heappop(minQ)
            if minQ:
                x = heapq.heappop(minQ)
                count[x] -= 1
                    
    while maxQ and count[-maxQ[0]] == 0:
        heapq.heappop(maxQ)
    while minQ and count[minQ[0]] == 0:
        heapq.heappop(minQ)

    if not minQ or not maxQ:
        return [0, 0]
    return [-maxQ[0], minQ[0]]
                
    
    