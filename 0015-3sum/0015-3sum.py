class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        answer = set()
        for i in range(len(nums)-2):
            target = -nums[i]

            left = i+1
            right = len(nums)-1

            while left < right:
                value = nums[left] + nums[right]
                if value == target:
                    answer.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                    left+=1
                    right-=1
                elif value < target:
                    left+=1
                else:
                    right -=1
        
        return [list(i) for i in answer]
