from collections import deque
class Solution:
    def findMin(self, nums: List[int]) -> int:
        q = deque(nums)

        while q[0] > q[-1]:
            q.append(q.popleft())
        
        return q[0]