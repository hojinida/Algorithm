class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = [chr(i) for i in range(65, 91)]
        answer = []

        while columnNumber > 0:
            columnNumber -= 1
            value = columnNumber % 26
            answer.append(alpha[value])
            columnNumber //= 26

        return "".join(reversed(answer))