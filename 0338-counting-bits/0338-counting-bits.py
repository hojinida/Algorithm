class Solution:
    def countBits(self, n: int) -> List[int]:
        array = [2 ** i for i in range(17)]
        pattern = [True for _ in range(17)]
        answer = []

        value = 1
        for i in range(n+1):
            if 2** value ==i:
                value+=1
            for j in range(1,value):
                if array[j] == 0:
                    array[j] = 2**j
                    pattern[j] = not pattern[j]
                array[j] -=1
            pattern[0] = not pattern[0]
            temp = 0
            for j in range(value):
                if pattern[j] : temp+=1
            
            answer.append(temp)

           
        return answer