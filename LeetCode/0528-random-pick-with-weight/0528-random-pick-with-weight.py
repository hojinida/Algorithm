import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_sum = 0
        total_sum = sum(w)
        
        for weight in w:
            current_sum += weight / total_sum * 100
            self.prefix_sum.append(current_sum)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.prefix_sum[-1]) 
        for i, val in enumerate(self.prefix_sum):
            if target < val:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()