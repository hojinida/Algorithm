from collections import deque
def solution(board):
    def findR(board):
        for i in range(len(board)):
          for j in range(len(board[0])):
            if board[i][j] == "R":
                return [i,j]
            
    answer = 0
    q = deque()
    visit = set()
    pattern = [[0,1],[1,0],[-1,0],[0,-1]]
    i,j = findR(board)
    q.append((i,j,0))

    while q:
        x,y,value = q.popleft()
        visit.add((x,y))
        if board[x][y] == "G":
            return value

        for px,py in pattern:
            rx,ry = x,y
            dx,dy = x,y
            while True:
                dx,dy = dx+px,dy+py
                if 0 > dx or len(board) <= dx or 0 > dy or len(board[0]) <= dy:
                    rx,ry = dx-px,dy-py
                    break
                elif board[dx][dy] == "D":
                    rx,ry = dx-px,dy-py
                    break
                    
            if (rx,ry) not in visit:
                q.append((rx,ry,value+1))          

    return -1