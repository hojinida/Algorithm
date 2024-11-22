from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pattern = [(0,1),(0,-1),(1,0),(-1,0)]
        row = len(board)
        col = len(board[0])
        wordLen = len(word)-1

        def backtracking(x,y,target):
            if board[x][y] != word[target]:
                return False
            
            if target == wordLen:
                return True
            
            temp = board[x][y]
            board[x][y] = "#"

            for px, py in pattern:
                dx, dy = x + px, y + py
                if 0 <= dx < row and 0 <= dy < col and board[dx][dy] != "#":
                    if backtracking(dx, dy, target + 1):
                        return True
        
            board[x][y] = temp
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtracking(i,j,0):
                        return True
        
        return False

            

