import heapq
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        hq = []

        for i in nums:
            heapq.heappush(hq,i**2)

        answer = []

        while hq:
            p = heapq.heappop(hq)
            answer.append(p)

        return answer