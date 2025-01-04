from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        answer = 0
        flag = False
        for i in count.values():
            if i//2 > 0:
                if i%2 == 1:
                    flag =True
                    answer+= (i - i%2)
                else:
                    answer+=i
            if i == 1:
                flag = True

        if flag : answer +=1

        return answer
