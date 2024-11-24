from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern = dict()

        for s in strs:
            count = frozenset(Counter(s).items())
            if count not in pattern:
                pattern[count] = []
            pattern[count].append(s)

        return [i for i in pattern.values()]
        
            