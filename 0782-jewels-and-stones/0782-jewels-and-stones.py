from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(stones)
        
        answer = 0
        for jewel in jewels:
            answer+=count[jewel]
        
        return answer