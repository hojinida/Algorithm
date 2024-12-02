class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        answer = []
        count = 0
        for row in range(m):
            temp = []
            for col in range(n):
                temp.append(original[(row*n)+col])
                count+=1
            answer.append(temp)
        
        return answer 