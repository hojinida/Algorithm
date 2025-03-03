def solution(s):
    if len(s) == 1:
        return 1
    answer = float('inf')

    for i in range(1,len(s)//2+1):
        tokens = []
        
        for j in range(0,len(s),i):
            tokens.append(s[j:j+i])
            
        index = 1
        result =0
        before = tokens[0]
       
        for token in tokens[1:]:
            if before != token:
                result += len(before)
                if index > 1:
                    result+=len(str(index))
                index = 1
            else:
                index+=1
            before = token
            
        result += len(before)
        
        if index > 1:
            result+=len(str(index))

        answer = min(answer,result)
    
    return answer