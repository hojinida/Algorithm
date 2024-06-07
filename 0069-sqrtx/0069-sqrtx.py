class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        index = 0
        while True:
            sqrt = index*index
            if sqrt == x:
                return index
            elif sqrt > x:
                return index -1 
            index+=1

