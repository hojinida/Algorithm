class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pattern = re.findall(r'[0-9]+|[a-zA-Z]', abbr)
        
        for part in pattern:
            if part.isdigit() and part.startswith('0'):
                return False

        length = len(word)
        answer= []
        index = 0
        for i in pattern:
            if index >= length:
                return False
            if i.isdigit():
                for _ in range(int(i)):
                    if index >= length:
                        return False
                    answer.append(word[index])
                    index+=1
            else:
                answer.append(i)
                index+=1
        
        answer = "".join(answer)
    
        if answer == word:
            return True
        else:
            return False
