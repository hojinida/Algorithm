class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pattern = dict()
     
        for n in nums:
            if n not in pattern:
                pattern[n] = 0
            pattern[n]+=1
        
        sortedItems = sorted(pattern.items(), key=lambda x: x[1], reverse=True)
        answer = []
        for i in range(k):
            answer.append(sortedItems[i][0])
        return answer