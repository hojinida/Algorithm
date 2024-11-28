class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row, first_col = False, False

        # 첫 번째 행과 열에 0이 있는지 확인
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row = True

        # 첫 번째 행과 열을 사용해 0 위치를 표시
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 표시된 위치에 따라 행과 열을 0으로 설정
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 첫 번째 행과 열 처리
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0