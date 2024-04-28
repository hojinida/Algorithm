class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tl = len(nums1)-1
        mp  =  m-1
        np  =  n-1
        while mp != -1 and np != -1:
            if nums1[mp] > nums2[np]:
                nums1[tl] = nums1[mp]
                mp-=1
            else:
                nums1[tl] = nums2[np]
                np-=1
            tl-=1
        
        while np >= 0:
            nums1[tl] = nums2[np]
            np -= 1
            tl -= 1

        
        