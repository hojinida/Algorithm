from collections import deque
def solution(stones, k):
    length = len(stones)
    q = deque()
    for i in range(k):
        while q and stones[q[-1]] < stones[i]:
            q.pop()
        q.append(i)
    
    for i in range(k,length):
        stones[i] = min(stones[i],stones[q[0]])
        
        if q and q[0] <= i - k:
            q.popleft()

        while q and stones[q[-1]] < stones[i]:
            q.pop()
        q.append(i)
    
    return max(stones[len(stones)-k:])
            
            