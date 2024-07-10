from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            pattern[key].append(s)

        return pattern.values()
        
        
            