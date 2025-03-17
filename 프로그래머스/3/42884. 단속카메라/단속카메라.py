def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    
    cctv = []
    for start,end in routes:
        flag = True
        for c in cctv:
            if start <= c and c<=end:
                flag=False
                break
        if flag:
            cctv.append(end)
    
    return len(cctv)