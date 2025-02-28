def solution(players, m, k):
    q = []
    max_players = 0
    answer = 0
    hour = 0
    for i in players:
        if q and q[0][1] == hour:
            max_players -= (q.pop(0)[0])
        i = i-max_players
        if i >= m:
            q.append([(i//m)*m,hour+k])
            answer+= (i//m)
            max_players += (i//m)*m
        hour+=1
        
    return answer