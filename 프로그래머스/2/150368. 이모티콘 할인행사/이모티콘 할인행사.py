def solution(users, emoticons):
    global answer
    answer =[0,0]
    
    def bfs(totals,eindex):
        global answer
        if len(emoticons) == eindex:
            plus = 0
            total = 0
            for t in range(len(totals)):
                if totals[t] >= users[t][1]:
                    plus += 1
                else:
                    total += totals[t]
                    
            if answer[0] < plus:
                answer[0] = plus
                answer[1] = total
            elif answer[0] == plus:
                answer[1] = max(total,answer[1])
                
            return
        else:
            for discount in [10,20,30,40]:
                newTotals = totals[:]
                for i in range(len(users)):
                    if users[i][0] <= discount:
                        newTotals[i] += (emoticons[eindex]*(1 - discount*0.01))
                bfs(newTotals,eindex+1)
    
    bfs([0] * len(users),0)
    
    return answer
    