class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1] ,reverse = True)
        answer = 0

        for boxType,unit in boxTypes:
            while truckSize > 0 and boxType >0:
                answer += unit
                truckSize-=1
                boxType-=1
        
        return answer
            