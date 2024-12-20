class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        beforeValue = 0
        for tax,percent in brackets:
            if income == 0:
                return answer

            value = min(income,(tax-beforeValue))
            answer += value * (percent / 100)
            income -= value
            beforeValue = tax
            
        return answer