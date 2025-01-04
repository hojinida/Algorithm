class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWaitingTime = 0
        currentTime = 0
        
        for arrivalTime, cookTime in customers:
            currentTime = max(currentTime, arrivalTime)
            totalWaitingTime += currentTime + cookTime - arrivalTime
            currentTime += cookTime
        
        return totalWaitingTime / len(customers)

        