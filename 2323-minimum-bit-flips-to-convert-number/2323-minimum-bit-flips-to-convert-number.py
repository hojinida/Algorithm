class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = [i for i in bin(start)[2:]] 
        goal = [i for i in bin(goal)[2:]]
        more = max(len(goal),len(start))

        start = ''.join(start).zfill(more)
        goal = ''.join(goal).zfill(more)

        answer = 0 

        for i,j in zip(start,goal):
            if i != j:
                answer+=1
        
        return answer