class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0 :
            return False
        if bin(n).count('1') == 1:
            return True
        return False