class Solution:
    def numberCount(self, a: int, b: int) -> int:
        answer = 0
        for i in range(a,b+1):
            if len(str(i)) == len(set([s for s in str(i)])):
                answer+=1
        return answer
