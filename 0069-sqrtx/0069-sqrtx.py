class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 0
    
        while True:
            temp = sqrt**2
            if temp == x:
                return sqrt
            elif temp > x:
                return sqrt-1
            sqrt+=1

