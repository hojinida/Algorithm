class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        pattern = {}

        for i in nums:
            if i not in pattern:
                pattern[i] = 0
            pattern[i]+=1
        
        maxFreq = max(pattern.values())

        answer =0
        for num,freq in pattern.items():
            if maxFreq == freq:
                answer += maxFreq

        return answer