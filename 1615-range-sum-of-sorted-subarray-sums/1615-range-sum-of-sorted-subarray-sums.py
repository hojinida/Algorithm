class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        answer = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                answer.append(sum(nums[i:j]))
        
        answer.sort()
        return sum(answer[left-1:right])%(10**9+7)

        