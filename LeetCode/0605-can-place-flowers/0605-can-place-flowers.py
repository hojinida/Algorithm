class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def jud(index):
            left = index-1
            right = index +1

            if left < 0 and right < len(flowerbed):
                if flowerbed[right] == 0:
                    return True
            elif right > len(flowerbed)-1 and left >= 0:
                if flowerbed[left] == 0:
                    return True
            elif left >= 0 and right < len(flowerbed):
                if flowerbed[right] == 0 and flowerbed[left] == 0:
                    return True
            else:
                return True
            return False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if jud(i):
                    flowerbed[i]= 1
                    n-=1
                if n == 0:
                    return True

        if n <= 0:
            return True
        
        return False