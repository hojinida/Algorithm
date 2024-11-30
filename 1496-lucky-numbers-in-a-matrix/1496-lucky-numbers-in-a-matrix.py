class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minCol = [float('inf') for _ in range(len(matrix))]
        maxRow = [0 for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                minCol[row] = min(minCol[row],matrix[row][col])
                maxRow[col] = max(maxRow[col],matrix[row][col])
        
        answer = []
        pattern = {}
        minCol+=maxRow
        
        for i in minCol:
            if i not in pattern:
                pattern[i] = 0
            else:
                answer.append(i)
        
        return answer
