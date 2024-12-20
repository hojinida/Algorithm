class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        pattern = {}

        length = 0
        for arr in grid:
            for i in arr:
                if i not in pattern:
                    pattern[i] = 0
                pattern[i]+=1
                length+=1

        repeat = []
        missing = []
        for i in range(1,length+1):
            if i not in pattern:
                missing.append(i)
            elif pattern[i] != 1:
                repeat.append(i)
        
        return repeat+missing

        
        