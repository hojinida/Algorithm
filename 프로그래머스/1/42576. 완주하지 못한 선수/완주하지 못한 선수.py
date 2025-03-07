def solution(participant, completion):
    pattern = {}
    
    for p in participant:
        if p not in pattern:
            pattern[p] = 0
        pattern[p]+=1

    for c in completion:
        if c not in pattern:
            return c
        else:
            pattern[c]-=1
            if pattern[c] == 0:
                pattern.pop(c)
                
    return list(pattern.keys())[0]