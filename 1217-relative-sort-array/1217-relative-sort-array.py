from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        answer = []
        for i in arr2:
            for _ in range(count[i]):
                answer.append(i)
            del(count[i])
        
        temp = []
        for i in count.keys():
            for _ in range(count[i]):
                temp.append(i)
        temp.sort()

        answer+=temp

        return answer