from collections import Counter, OrderedDict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
     
        count = Counter(arr)

        ordered_count = OrderedDict((key, val) for key, val in count.items() if val == 1)
        if len(ordered_count) >= k:
            return list(ordered_count.keys())[k-1]
        return ""