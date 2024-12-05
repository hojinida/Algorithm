from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        pattern = Counter(s1.split(" ") + s2.split(" "))
        return [key for key, value in pattern.items() if value == 1]