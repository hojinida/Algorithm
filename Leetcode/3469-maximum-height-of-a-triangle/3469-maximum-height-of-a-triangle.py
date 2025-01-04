class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def find(fRed,fBlue,start):
            count = 1
            result = 0
            while True:
                if start == True:
                    if (fRed - count) < 0:
                        return result
                    fRed-= count
                else:
                    if (fBlue - count) <0:
                        return result
                    fBlue -= count
                count+=1
                result+=1
                start = not start
        
        return max(find(red,blue,True),find(red,blue,False))