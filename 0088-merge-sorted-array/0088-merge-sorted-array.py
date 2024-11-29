class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = len(nums1) - 1 
        left = m - 1          
        index = n - 1     

        while index >= 0:  
            if left >= 0 and nums1[left] > nums2[index]:
                nums1[right] = nums1[left]
                left -= 1
            else:
                nums1[right] = nums2[index]
                index -= 1
            right -= 1

        
            
        