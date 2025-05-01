def solution(n):
    a = [i for i in str(n)]
    a.sort(reverse = True)
    
    return int("".join(a))