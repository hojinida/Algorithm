from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = deque(word1)
        word2 = deque(word2)

        answer = []
        while True:
            if word1:
                answer.append(word1.popleft())
            else:
                break
            
            if word2:
                answer.append(word2.popleft())
            else:
                break
        answer = "".join(answer)
        if word1:
            answer+= "".join(word1)
        elif word2:
            answer+= "".join(word2)

        return answer
