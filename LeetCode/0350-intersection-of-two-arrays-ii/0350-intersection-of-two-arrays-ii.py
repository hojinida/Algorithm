class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pattern= {}

        for i in nums1:
            if i not in pattern:
                pattern[i] = 0
            pattern[i] +=1

        
        answer = []
        for i in nums2:
            if i in pattern and pattern[i] > 0:
                answer.append(i)
                pattern[i] -=1
        
        return answer