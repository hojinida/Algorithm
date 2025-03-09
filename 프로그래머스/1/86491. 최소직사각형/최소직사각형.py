def solution(sizes):
    mx = []
    my = []
    for x,y in sizes:
        mx.append(max(x,y))
        my.append(min(x,y))
    
    
    return max(mx) * max(my)