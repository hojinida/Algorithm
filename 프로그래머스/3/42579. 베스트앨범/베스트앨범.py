from collections import defaultdict
import heapq
def solution(genres, plays):
    pattern = defaultdict(list)
    
    for i,(gen,play) in enumerate(zip(genres, plays)):
        heapq.heappush(pattern[gen],(-play,i))
    
    q = []
    for key,value in pattern.items():
        total = sum(-i[0] for i in value)
        heapq.heappush(q,(-total,key))
    
    answer = []
    while q:
        key,value = heapq.heappop(q)
        for _ in range(2):
            if pattern[value]:
                answer.append(heapq.heappop(pattern[value])[1])
    
    return answer
    