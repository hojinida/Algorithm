from collections import deque
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        wordLen = len(word)
        sequenceLen = len(sequence)

        q = deque()

        for i in range(sequenceLen):
            if i + wordLen-1 >= sequenceLen:
                break
            if sequence[i] == word[0]:
                if i+wordLen <= sequenceLen and sequence[i:i+wordLen] == word:
                    q.append(i)
        print(q)
        answer = 0
        while q:
            temp =1
            p = q.popleft()

            for i in q:
                if i == p+(wordLen*temp):
                    temp+=1
            answer = max(answer,temp)

        return answer