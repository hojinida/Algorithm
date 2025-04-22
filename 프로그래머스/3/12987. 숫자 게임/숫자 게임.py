def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    while B and A:
        value = B.pop()
        while A:
            v = A.pop()
            if value > v:
                answer+=1
                break
    
    return answer