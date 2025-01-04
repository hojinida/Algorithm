class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        before = {}

        answer = []
        for i in range(len(t)):
            if t[i] in before:
                answer.append(before[t[i]])
            else:
                if s[i] in before.values():
                    return False
                before[t[i]] = s[i]
                answer.append(s[i])
        
        if "".join(answer) == s:
            return True
        else:
            return False
