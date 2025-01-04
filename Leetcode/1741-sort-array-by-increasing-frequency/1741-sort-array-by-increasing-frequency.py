from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        answer = []

        for key,value in sorted(count.items(), key = lambda x: (x[1], -x[0])):
            for i in range(value):
                answer.append(key)
        
        return answer