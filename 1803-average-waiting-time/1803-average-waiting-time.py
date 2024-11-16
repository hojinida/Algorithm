class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWaitTime = 0
        excuteTime = 0
        
        for arrivalTime, waitTime in customers:
            waitingTime = 0
            if excuteTime > arrivalTime:
                waitingTime = excuteTime -arrivalTime
            totalWaitTime += waitTime + waitingTime
            excuteTime = arrivalTime+waitTime+waitingTime
        
        return totalWaitTime/len(customers)

        