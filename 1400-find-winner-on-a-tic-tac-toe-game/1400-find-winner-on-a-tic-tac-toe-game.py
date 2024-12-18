class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        pattern = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[-1,1],[-1,-1],[1,1]]
        turn = True
        graph = [["" for _ in range(3)]for _ in range(3)]

        for move in moves:
            if turn:
                graph[move[0]][move[1]] = "X"
            else:
                graph[move[0]][move[1]] = "O"
            turn = not turn
        
        def dfs(x,y,target):
            for px,py in pattern:
                dx,dy = x+px , y+py
                if 0<=dx<3 and 0<=dy<3 and graph[dx][dy] == target:
                    dx, dy = dx+px,dy+py
                    if 0<=dx<3 and 0<=dy<3 and graph[dx][dy] == target:
                        if target =="X":
                            return "A"
                        return "B"
            return ""

        for i in range(3):
            for j in range(3):
                if graph[i][j] in ("X","O"):
                    result =dfs(i,j,graph[i][j])
                    if result != "":
                        return result
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"