from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            pattern[key].append(s)

        return pattern.values()
        
        
            