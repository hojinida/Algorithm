class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        preC2 = cost[0] # 전전 값
        preC = cost[1] # 전 값
        
        for i in range(2,len(cost)):
            value = min(preC2+cost[i],preC+cost[i])
            preC2 = preC
            preC = value
        
        return min(preC,preC2)
