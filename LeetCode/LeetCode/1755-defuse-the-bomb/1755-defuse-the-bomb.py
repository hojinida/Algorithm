class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []

        if k > 0:
            for i in range(len(code)):
                hap = 0
                for j in range(1,k+1):
                    hap+= code[(i+j)%len(code)]
                answer.append(hap)
        elif k < 0:
            for i in range(len(code)):
                hap = 0
                for j in range(1,abs(k)+1):
                    hap+= code[(i-j)%len(code)]
                answer.append(hap)
        else:
            answer = [0 for _ in range(len(code))]

        return answer
