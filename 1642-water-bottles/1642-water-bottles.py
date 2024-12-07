class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0

        binBottles = 0
        while numBottles > 0:
            answer += numBottles
            binBottles += numBottles
            numBottles = binBottles // numExchange
            binBottles %= numExchange

        return answer