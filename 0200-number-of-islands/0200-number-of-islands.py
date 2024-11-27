from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        answer = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    answer+=1
                    while q:
                        (x,y) = q.popleft()
                        
                        for px,py in [(0,1),(0,-1),(1,0),(-1,0)]:
                            dx,dy = x+px, y+py
                            if 0<=dx< rows and 0<=dy<cols and (dx,dy) not in visited:
                                if grid[dx][dy] == "1":
                                    visited.add((dx,dy))
                                    q.append((dx,dy))
            

        return answer          

