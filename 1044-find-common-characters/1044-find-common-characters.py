class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        pattern = words[0]

        answer = []
        flag = []
        for s in pattern:
            if s in flag: continue
            temp=[]
            for word in words:
                temp.append(word.count(s))
            value= min(temp)
            for i in range(value):
                answer.append(s)
            flag.append(s)
      
        return answer