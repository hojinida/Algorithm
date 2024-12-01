class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        answer = 0
        for s in arr:
            if s % 2 == 1:
                answer+=1
            else:
                answer = 0
            if answer == 3:
                return True
        
        return False