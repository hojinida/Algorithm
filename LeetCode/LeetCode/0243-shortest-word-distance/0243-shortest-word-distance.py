class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1Index = []
        word2index = []

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1Index.append(i)
            elif wordsDict[i] == word2:
                word2index.append(i)
        
        answer = float('inf')

        for i in word1Index:
            for j in word2index:
                answer = min(answer,abs(i-j))
        
        return answer