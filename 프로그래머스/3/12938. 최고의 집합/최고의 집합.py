def solution(n, s):
    if s//n == 0:
        return [-1]
    
    base = s // n
    rem  = s % n
    
    result = [base] * (n - rem) + [base + 1] * rem
    return result