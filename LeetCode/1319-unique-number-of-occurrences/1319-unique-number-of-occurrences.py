class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        pattern = {}
        for i in arr:
            if i in pattern:
                pattern[i]+=1
            else:
                pattern[i] = 0
        answer = []
        for i in pattern.values():
            if i in answer:
                return False
            answer.append(i)
        
        return True
        
            