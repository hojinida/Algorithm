from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        answer = 0
        for i in s:
            if i not in q:
                q.append(i)
            else:
                lenth = len(q)
                q.popleft()
                if lenth > answer:
                    answer=lenth
                while i in q:
                    q.popleft()
                q.append(i)
        print(q)
        if len(q) > answer:
            answer = len(q)
        return answer


