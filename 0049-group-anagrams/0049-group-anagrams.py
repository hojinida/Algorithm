from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern = defaultdict(list)

        for s in strs:
            count = frozenset(Counter(s).items())
            pattern[count].append(s)

        return [i for i in pattern.values()]
        
            