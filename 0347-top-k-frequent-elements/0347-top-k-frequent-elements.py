from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
