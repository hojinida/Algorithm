from itertools import combinations
def solution(relation):
    answer = 0
    database = set()
    
    for j in range(1,len(relation[0])+1):
        for i in list(combinations([i for i in range(len(relation[0]))],j)):
            skip = False
            for d in database:
                if set(d).issubset(i):
                    skip = True
                    break
            if skip:
                continue
            
            col = set()
            
            flag = True
            for r in relation:
                temp = tuple(r[idx] for idx in i)

                if temp in col:
                    flag = False
                    break
                col.add(temp)
            
            if flag :
                database.add(i)
            
    return len(database)