from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        if image[sr][sc] != color:
            q.append((sr,sc))
        before = image[sr][sc]

        while q:
            x,y = q.popleft()
            image[x][y] = color
            
            for px,py in [[0,1],[0,-1],[1,0],[-1,0]]:
                dx,dy = x+px,y+py
                if 0<=dx<len(image) and 0<=dy<len(image[0]):
                    if image[dx][dy] == before:
                        q.append((dx,dy))
        
        return image