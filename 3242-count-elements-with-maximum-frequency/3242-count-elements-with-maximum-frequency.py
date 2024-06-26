class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        pattern = {}

        maxFreq = 0
        for i in nums:
            if i not in pattern:
                pattern[i] = 0
            pattern[i] += 1
            maxFreq = max(maxFreq, pattern[i])

        # 최대 빈도와 일치하는 요소의 빈도 합산
        answer = 0
        for num, freq in pattern.items():
            if maxFreq == freq:
                answer += freq

        return answer