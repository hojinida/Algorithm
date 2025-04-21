import heapq
def solution(n, works):
    q = [-w for w in works]
    heapq.heapify(q)
    
    for i in range(n):
        if not q:
            break
        p = -heapq.heappop(q)
        p-=1
        if p != 0:
            heapq.heappush(q,-p)
    
    answer = 0
    
    for i in q:
        answer += (i**2)
    
    return answer