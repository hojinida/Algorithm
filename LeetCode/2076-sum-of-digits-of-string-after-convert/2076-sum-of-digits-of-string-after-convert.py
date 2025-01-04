class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = []
        for i in s:
            convert.append(str(ord(i)-96))

        for _ in range(k):
            transform = 0
            for i in "".join(convert):
                transform+=int(i)
            convert = str(transform)
        
        return int(convert)