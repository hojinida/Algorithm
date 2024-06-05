class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits)-1,-1,-1):
            c = digits[i]+plus
            if c > 9:
                c = 0
                plus+1
            else:
                plus = 0
            
            digits[i] =  c
        if plus == 1:
            digits.insert(0,plus)
        return digits