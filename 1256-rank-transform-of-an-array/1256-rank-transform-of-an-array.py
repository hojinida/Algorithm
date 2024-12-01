class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        pattern = {key:index+1 for index,key in enumerate(sorted(set(arr)))}

        answer = []
        for i in arr:
            answer.append(pattern[i])
        
        return answer