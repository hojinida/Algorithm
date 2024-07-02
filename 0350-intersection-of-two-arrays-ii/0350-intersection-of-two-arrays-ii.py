class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pattern= {}
        pattern2 = {}

        for i in nums1:
            if i not in pattern:
                pattern[i] = 0
            pattern[i] +=1

        for i in nums2:
            if i not in pattern2:
                pattern2[i] = 0
            pattern2[i] +=1

        answer = []
        for i in pattern:
            if i in pattern2:
                for j in range(min(pattern[i],pattern2[i])):
                    answer.append(i)
        
        return answer