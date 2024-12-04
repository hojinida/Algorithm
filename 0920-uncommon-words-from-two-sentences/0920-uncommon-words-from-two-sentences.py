class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        pattern = dict()
        
        answer = []
        for s in s1.split(" "):
            if s not in pattern:
                pattern[s] = 1
            else:
                pattern[s] += 1
                
        for s in s2.split(" "):
            if s not in pattern:
                pattern[s] = 1
            else:
                pattern[s] += 1
        
        for key,value in pattern.items():
            if value < 2:
                answer.append(key)
        
        return answer