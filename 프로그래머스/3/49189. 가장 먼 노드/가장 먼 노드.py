from collections import defaultdict
from collections import deque
def solution(n, edge):
    answer = defaultdict(list)
    graph = defaultdict(list)
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    q = deque()
    q.append((1,0))
    visited = set()
    visited.add(1)
    
    while q:
        p,v = q.popleft()
        answer[v].append(p)
        
        for i in graph[p]:
            if i not in visited:
                visited.add(i)
                q.append((i,v+1))
            
    return len(answer[max(answer.keys())])