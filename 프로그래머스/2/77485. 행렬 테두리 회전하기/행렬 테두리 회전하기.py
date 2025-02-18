def solution(rows, columns, queries):
    answer = []
    arr = [[i+(columns*j) for i in range(1,columns+1)] for j in range(rows)]
    
    def circle(x,y,px,py,arr):
        dx,dy = x,y
        temp = arr[x][y]
        result = []
        result.append(temp)
        while dy < py:
            dy+=1
            arr[dx][dy],temp = temp,arr[dx][dy]
            result.append(temp)
        while dx < px:
            dx+=1
            arr[dx][dy],temp = temp,arr[dx][dy]
            result.append(temp)
        while dy > y:
            dy-=1
            arr[dx][dy],temp = temp,arr[dx][dy]
            result.append(temp)
        while dx > x:
            dx-=1
            arr[dx][dy],temp = temp,arr[dx][dy]
            result.append(temp)
        return min(result)
    
    answer = []
    for querie in queries:
        answer.append(circle(querie[0]-1,querie[1]-1,querie[2]-1,querie[3]-1,arr))
        
        
    return answer