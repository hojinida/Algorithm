class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        answer = []
        before = ""
        
        for word,i in zip(words,groups):
            if i != before:
                answer.append(word)
            before = i
        
        return answer