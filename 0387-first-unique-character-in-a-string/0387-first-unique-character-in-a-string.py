class Solution:
    def firstUniqChar(self, s: str) -> int:
        pattern = {i:1 for i in s}

        for i in s:
            if i in pattern:
                if pattern[i] == 0:
                    del(pattern[i])
                else:
                    pattern[i] -=1

        for i in range(len(s)):
            if s[i] in pattern:
                return i

        return -1