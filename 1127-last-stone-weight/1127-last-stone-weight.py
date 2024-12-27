import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)
        
        while q:
            if len(q) < 2:
                return -q[0]

            y = -heapq.heappop(q)
            x = -heapq.heappop(q)

            if x == y:
                continue
            else:
                heapq.heappush(q,-(y-x))
        
        return 0
