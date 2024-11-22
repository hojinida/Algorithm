class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minIndex = 0
        maxIndex = 0

        answer = 0
        for i in range(1,len(prices)):
            if minIndex < maxIndex:
                answer = max(answer,(prices[maxIndex] - prices[minIndex]))
            else:
                maxIndex = minIndex

            if prices[minIndex] > prices[i]:
                minIndex = i
            if prices[maxIndex] < prices[i]:
                maxIndex = i

        if minIndex < maxIndex:
            answer = max(answer,(prices[maxIndex] - prices[minIndex]))
        return answer