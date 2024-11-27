from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        q = deque()
        pattern = set()

        for i in range(len(s)):
            if s[i] in pattern:
                maxLen = max(maxLen,len(q))
                while q:
                    poped = q.popleft()
                    pattern.remove(poped)
                    if poped == s[i]:
                        break
   
            q.append(s[i])
            pattern.add(s[i])

        maxLen = max(maxLen,len(q))

        return maxLen