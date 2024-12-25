from collections import OrderedDict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pattern = OrderedDict([i,-1] for i in nums1)
        
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                if nums2[i] < nums2[j]:
                    if nums2[i] in pattern:
                        pattern[nums2[i]] = nums2[j]
                    break
        
        answer = []

        for key,value in pattern.items():
            answer.append(value)
            
        return answer
        
        

        