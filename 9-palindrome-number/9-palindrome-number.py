class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if "".join(reversed(list(str(x)))) == str(x) else False