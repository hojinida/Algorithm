class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pattern = {}

        for i in s:
            if i in pattern:
                pattern[i] += 1
            else:
                pattern[i] = 1
        
        for i in t:
            if i in pattern:
                pattern[i] -= 1
                if pattern[i] == 0:
                    del(pattern[i])
            else:
                return False

        if pattern:
            return False
        else:
            return True

