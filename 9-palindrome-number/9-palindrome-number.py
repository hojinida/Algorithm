class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return True if "".join(reversed(list(x)))== x else False