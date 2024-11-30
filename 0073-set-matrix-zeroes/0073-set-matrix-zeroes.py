class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_positions = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        for x, y in zero_positions:
            for col in range(cols):
                matrix[x][col] = 0
            for row in range(rows):
                matrix[row][y] = 0