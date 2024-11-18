class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(n):
            result = 0
            while n>0:
                if n%2 == 1:
                    result+=1
                n //= 2
            return result

        answer = []
        for i in range(n+1):
            answer.append(countBit(i))
        return answer

            