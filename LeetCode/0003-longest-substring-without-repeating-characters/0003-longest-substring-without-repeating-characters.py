class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        start = 0
        pattern = {}

        for end in range(len(s)):
            if s[end] in pattern and pattern[s[end]] >= start:
                start = pattern[s[end]] + 1
            
            pattern[s[end]] = end
            maxLen = max(maxLen,end - start+1)
        
        return maxLen