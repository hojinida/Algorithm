from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        target = Counter(t)
        if counter == target:
            return True
        return False
