from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern = defaultdict(list)

        for s in strs:
            sorted_key = ''.join(sorted(s))
            pattern[sorted_key].append(s)

        return [group for group in pattern.values()]
        
            