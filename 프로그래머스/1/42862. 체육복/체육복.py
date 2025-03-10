def solution(n, lost, reserve): 
    answer = [1 for _ in range(n)]
    for i in lost:
        answer[i-1] -= 1
    for r in reserve:
        answer[r-1] += 1
    
    for i in range(n):
        if answer[i] == 0:
            if i-1 >=0:
                if answer[i-1] == 2:
                    answer[i-1] =1
                    answer[i]=1
                    continue
            if i+1 < n:
                if answer[i+1] == 2:
                    answer[i+1] =1
                    answer[i] = 1
    result = 0
    for i in answer:
        if i >= 1:
            result+=1
                
    return result