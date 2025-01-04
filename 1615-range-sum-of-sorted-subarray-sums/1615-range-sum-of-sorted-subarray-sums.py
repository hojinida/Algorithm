import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Prefix Sum 계산
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        
        # Step 2: 모든 부분합 계산
        subarray_sums = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == 0:
                    subarray_sums.append(prefix[j])
                else:
                    subarray_sums.append(prefix[j] - prefix[i - 1])
        
        # Step 3: 정렬 후 필요한 값만 합산
        subarray_sums.sort()
        return sum(subarray_sums[left - 1:right]) % MOD