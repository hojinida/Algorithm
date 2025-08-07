from collections import deque
def solution(priorities, location):
    p = {}
    
    for i in priorities:
        if i not in p:
            p[i] = 0
        p[i] +=1
    
    q = deque([v,i] for i,v in enumerate(priorities))
    
    answer = 0
    while q:
        value,index = q.popleft()
        
        if value == max(p.keys()):
            p[value] -=1
            if p[value] == 0:
                del p[value]
            answer+=1
            if index == location:
                return answer
        else:
            q.append([value,index])
                