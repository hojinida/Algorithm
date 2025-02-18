import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    for enem in enemy:
        if len(q) < k:
            heapq.heappush(q,enem)
        elif q[0] < enem and q[0] <= n: 
            n -= heapq.heappop(q) 
            heapq.heappush(q, enem) 
        elif n >= enem:
            n-=enem
        else:
            break
        answer+=1
    return answer