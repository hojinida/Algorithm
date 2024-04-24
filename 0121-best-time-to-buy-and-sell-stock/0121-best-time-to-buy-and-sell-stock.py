class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        value = 1000000

        for i in prices:
            if value > i:
                value = i
            elif answer < (i-value):
                answer = i-value
        
        return answer