class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0 for _ in range(n)] for _ in range(n)]
        number = 0

        top,bottom = 0,n-1
        left,right = 0,n-1

        while top <= bottom and left <= right:
            for col in range(left,right+1):
                number+=1
                answer[top][col] = number
            top+=1
            
            for row in range(top,bottom+1):
                number+=1
                answer[row][right] = number
            right-=1

            if left <= right:
                for col in range(right,left-1,-1):
                    number+=1
                    answer[bottom][col] = number
                bottom-=1

            if top <= bottom:
                for row in range(bottom,top-1,-1):
                    number+=1
                    answer[row][left] = number
                left+=1
        
        return answer