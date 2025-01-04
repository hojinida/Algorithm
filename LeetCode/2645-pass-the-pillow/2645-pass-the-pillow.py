class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cicle = time // (n-1)
        time %= (n-1)

        if cicle % 2 == 0:
            return 1 + time
        else:
            return n - time