def solution(players, m, k):
    q = []
    
    server = {}
    server[100] = 1
    
    answer = 0
    for time,player in enumerate(players):
        if time - k in server:
            del server[time-k]
            
        num = sum(server.values()) * m
        if player // num > 0:
            result = (player - num) // m
            server[time] = result+1
            answer+=result+1
    
    return answer
    
            
            
    