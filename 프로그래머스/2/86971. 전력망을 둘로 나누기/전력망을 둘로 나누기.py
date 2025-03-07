from collections import defaultdict

def search(index,visit,graph):
    count =1
    for i in graph[index]:
        if i not in visit:
            visit.add(i)
            count += search(i,visit,graph)
    
    return count
            
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    
    for s,e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    for s,e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        
    
        visited = set()
        visited.add(s)
        one =search(s,visited,graph)
        visited = set()
        visited.add(e)
        two =search(e,visited,graph)
        answer = min(answer,abs(one-two))
        graph[s].append(e)
        graph[e].append(s)
    
    return answer
        
        
        
        
    