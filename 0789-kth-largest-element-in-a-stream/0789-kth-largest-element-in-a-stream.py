import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = []
        for num in nums:
            heapq.heappush(self.q, num)
            if len(self.q) > k: 
                heapq.heappop(self.q)


    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)