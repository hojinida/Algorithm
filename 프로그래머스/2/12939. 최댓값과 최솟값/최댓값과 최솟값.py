def solution(s):
    values = [int(i) for i in s.split()]
    
    return str(min(values))+" "+str(max(values))
    