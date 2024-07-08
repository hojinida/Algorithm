from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        q = deque()
        pattern = [(0,1),(1,0),(-1,0),(0,-1)]
        answer = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=="1":
                    visited.add((i,j))
                    q.append((i,j))
        
                    while q:
                        p = q.pop()
                   
                        for x,y in pattern:
                            dx = p[0] + x
                            dy = p[1] + y

                            if 0<= dx < len(grid) and 0 <= dy <len(grid[0]) and (dx,dy) not in visited:
                                if grid[dx][dy] == "1":
                                    q.append((dx,dy))
                                visited.add((dx,dy))
                    answer+=1

        return answer
                        

