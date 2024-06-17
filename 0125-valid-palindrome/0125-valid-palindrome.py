class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
        s = "".join(i.lower() if i.isupper() else i for i in s)
        
        ls = len(s)
        mid = ls//2
        if ls == 1:
            return True
        if ls%2 == 0:
            if s[0:mid] == s[:mid-1:-1]:
                return True
        else:
            if s[0:mid] == s[:mid:-1]:
                return True

        return False
