import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        heap = []
        
        for i in range(n):
            heapq.heappush(heap, (nums[i], i + 1))
        
        answer = 0
        for k in range(1, right + 1):
            val, idx = heapq.heappop(heap)
            if k >= left:
                answer = (answer + val) % mod
            if idx < n:
                heapq.heappush(heap, (val + nums[idx], idx + 1))
        
        return answer