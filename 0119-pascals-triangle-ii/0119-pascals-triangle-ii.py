class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[1]for _ in range(34)]
        answer[0]=[1]
        answer[1]=[1,1]

        for i in range(2,rowIndex+1):
            for d in range((len(answer[i-1])-1)):
                answer[i].append(answer[i-1][d]+answer[i-1][d+1])
            answer[i].append(1)
    
        return answer[rowIndex]