class Solution:
    def numberCount(self, a: int, b: int) -> int:
        def isUnique(num: int) -> bool:
            seen = set()
            while num > 0:
                digit = num % 10
                if digit in seen:
                    return False
                seen.add(digit)
                num //= 10
            return True

        return sum(1 for i in range(a, b + 1) if isUnique(i))