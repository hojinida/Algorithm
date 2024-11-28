class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack = []

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    stack.append((i,j))

        for x,y in stack:
            left = [x,y-1]
            right = [x,y+1]
            up = [x-1,y]
            down = [x+1,y]
            while left[1] >=0 or right[1] < cols or up[0] >=0 or down[0] < rows:
                if left[1] >= 0:
                    matrix[left[0]][left[1]] = 0
                    left[1]-=1
                if right[1] < cols:
                    matrix[right[0]][right[1]] = 0
                    right[1] +=1
                if up[0] >= 0:
                    matrix[up[0]][up[1]] = 0
                    up[0]-=1
                if down[0] <rows:
                    matrix[down[0]][down[1]] = 0
                    down[0]+=1