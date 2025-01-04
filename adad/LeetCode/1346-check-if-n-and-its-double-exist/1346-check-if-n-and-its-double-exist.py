class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pattern = {}

        for i in arr:
            if i/2 in pattern:
                return True
            elif i*2 in pattern:
                return True
            
            pattern[i] = 0
        return False