from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        l = 0
        max_len = 0
        for r in range(len(s)):
            counts[s[r]]+=1

            max_freq = max(counts.values())

            if (r - l +1) - max_freq > k:
                counts[s[l]]-=1
                l+=1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
        
                