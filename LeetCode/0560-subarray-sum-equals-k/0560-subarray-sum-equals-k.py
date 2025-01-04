from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pattern = defaultdict(int)
        pattern[0]=1

        answer = 0
        cSum = 0
        for num in nums:
            cSum+=num

            if cSum - k in pattern:
                answer += pattern[cSum - k]

            pattern[cSum] += 1

        return answer