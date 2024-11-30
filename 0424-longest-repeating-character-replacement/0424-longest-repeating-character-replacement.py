from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        l = 0
        max_len = 0
        max_freq = 0  # 최빈 문자 개수를 저장

        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])  # 갱신된 최빈 문자 개수 업데이트

            # 윈도우 크기가 조건을 초과하면 왼쪽 포인터 이동
            if (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            # 최대 길이 갱신
            max_len = max(max_len, r - l + 1)
        
        return max_len
        
                