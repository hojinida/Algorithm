from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        q = deque(intervals)

        answer = []
        while q:
            p1 = q.popleft()
            if not q:
                answer.append(p1)
                break
            if p1[1] >= q[0][0]:
                p1 = [p1[0],max(p1[1],q[0][1])]
                q.popleft()
                q.appendleft(p1)
            else:
                answer.append(p1)

        return answer
        