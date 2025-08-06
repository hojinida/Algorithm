from collections import deque
def solution(want, number, discount):
    want = {food:num for food,num in zip(want,number)}
    q = deque()
    answer = 0
    
    for food in discount:
        if len(q) == 10:
            p = q.popleft()
            if p in want:
                want[p]+=1
        
        q.append(food)
        if food in want:
            want[food]-=1
            
        flag = True
        for value in want.values():
            if value > 0:
                flag = False
                break
        if flag:
            answer+=1
    
    return answer
            