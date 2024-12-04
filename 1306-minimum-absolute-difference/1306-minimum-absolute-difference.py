class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        answer = set()
        pattern = {i for i in arr}
        
        arr.sort()
        minValue = float('inf')
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) < minValue:
                minValue = abs(arr[i] - arr[i+1])
        
        for i in pattern:
            if i+minValue in pattern:
                answer.add((i,i+minValue))
            elif i-minValue in pattern:
                answer.add((i-minValue,i))
        
        return sorted(answer)
            