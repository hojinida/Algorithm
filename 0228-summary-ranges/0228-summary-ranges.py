class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        left = 0
        right = 1

        while right < len(nums):
            if nums[right-1]+1 != nums[right]:
                if right-1 == left:
                    answer.append(str(nums[left]))
                else:
                    answer.append(str(nums[left]) + "->" + str(nums[right-1]))
                left = right
            right+=1
            
        if left < len(nums):
            if right-1 == left:
                answer.append(str(nums[left]))
            else:
                answer.append(str(nums[left]) + "->" + str(nums[right-1]))

        return answer