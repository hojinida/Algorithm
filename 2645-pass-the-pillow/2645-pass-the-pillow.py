class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dir = True

        answer =1
        while time > 0:
            if dir:
                answer+=1
            else:
                answer-=1
            
            if answer == n or answer == 1:
                dir = not dir
            time-=1
        
        return answer