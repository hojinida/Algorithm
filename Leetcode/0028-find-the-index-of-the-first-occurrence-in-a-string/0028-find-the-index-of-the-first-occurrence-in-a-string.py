class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        hlength = len(haystack)

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i+length <= hlength+1 and haystack[i:i+length] == needle:
                    return i

        return -1
        