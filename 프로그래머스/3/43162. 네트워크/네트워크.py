from collections import defaultdict
def search(key,visited,network):
    for i in network[key]:
        if i not in visited:
            visited.add(i)
            search(i,visited,network)
    return 1
    
    
def solution(n, computers):
    answer = 0
    network = defaultdict(list)
    
    for n,computer in enumerate(computers):
        for i,c in enumerate(computer):
            if i != n:
                if c== 1:
                    network[n].append(i)
        if n not in network:
            network[n] = []
    visited = set()
    for key in network.keys():
        if key not in visited:
            answer += search(key,visited,network)
    
    return answer