class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        pattern = {}

        for one,two in edges:
            if one in pattern:
                return one
            if two in pattern:
                return two
            pattern[one] = 1
            pattern[two] = 1
    