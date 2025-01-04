import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.findall(r'\b[a-z]+\b', paragraph.lower())

        answer = Counter(paragraph)
    
        for key,_ in sorted(answer.items(),key = lambda x: x[1],reverse= True):
            if key not in banned:
                return key
        

        