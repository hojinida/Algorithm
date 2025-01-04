class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1] ,reverse = True)
        answer = 0

        for boxType,unit in boxTypes:
            resultBox = min(boxType,truckSize)
            answer += unit*resultBox
            truckSize -= resultBox
            
            if truckSize == 0:
                break
        
        return answer
            