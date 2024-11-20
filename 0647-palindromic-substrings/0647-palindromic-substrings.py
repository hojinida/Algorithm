class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindromic(s):
            return s == s[::-1]

        answer = 0
        length = len(s)
        for i in range(1,length + 1):
            for j in range(length - i + 1):
                if isPalindromic(s[j:j+i]):
                    answer+=1

        return answer
                
        