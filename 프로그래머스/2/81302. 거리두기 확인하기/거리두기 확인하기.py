def solution(places):
    pattern = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def judg(place,x,y):
        for px,py in pattern:
            dx,dy = px+x, py+y
            if 0<= dx < 5 and 0<= dy <5:
                if place[dx][dy] == "P":
                    return False
                elif place[dx][dy] ==  "X":
                    continue
                else:
                    for kx,ky in pattern:
                        jx,jy = dx+kx , dy+ky
                        if (jx,jy) != (x,y) and 0<= jx < 5 and 0<= jy <5:
                            if place[jx][jy] == "P":
                                return False
        return True
                            
    def distance(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if not judg(place,i,j):
                        return 0
        return 1
    
    answer = []
    for place in places:
        answer.append(distance(place))
    return answer