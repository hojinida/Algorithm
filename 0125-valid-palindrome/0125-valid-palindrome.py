class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 영숫자 필터링 및 소문자 변환
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        
        # 투 포인터로 회문 확인
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True