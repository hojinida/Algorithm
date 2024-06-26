from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        pattern = [(0,1),(1,0),(-1,0),(0,-1)]
        lengthi = len(grid)
        lengthj = len(grid[0])
        visited = set()

        q = deque([])

        flag = False
        for i in range(lengthi):
            if flag : break
            for j in range(lengthj):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    q.append((i,j))
                    flag= True
                    break

        answer = 0
       
        while q:
            pi, pj = q.pop()

            temp = 0
            for i,j in pattern:
                di = pi+i
                dj = pj+j
                if 0<=di<lengthi and 0<=dj<lengthj and (di,dj) not in visited and grid[di][dj] == 1:
                    visited.add((di,dj))
                    q.append((di,dj))
                elif 0 > di or di >= lengthi or 0 > dj or dj >= lengthj or (0<=di<lengthi and 0<=dj<lengthj and grid[di][dj] != 1):
                    temp+=1
            answer+=temp

        return answer
        