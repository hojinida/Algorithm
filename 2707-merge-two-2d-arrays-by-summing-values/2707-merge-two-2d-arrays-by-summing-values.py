class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pattern = {}
        
        for id,value in nums1+nums2:
            if id not in pattern:
                pattern[id] = 0
            pattern[id] += value

        answer = []

        for id,value in sorted(pattern.items(),key = lambda x: x[0]):
            answer.append([id,value])
        
        return answer