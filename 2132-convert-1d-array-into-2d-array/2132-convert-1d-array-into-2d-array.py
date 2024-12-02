class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        answer = []
        count = 0
        for row in range(m):
            temp = []
            for col in range(n):
                if (row*n)+col >= len(original):
                    return []
                temp.append(original[(row*n)+col])
                count+=1
            answer.append(temp)
        
        return answer if count == len(original) else []