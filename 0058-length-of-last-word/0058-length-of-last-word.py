class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)

        answer= 0

        for i in range(length-1,-1,-1):
            if s[i].isalpha():
                answer +=1
            elif answer != 0 :
                return answer


        return answer
