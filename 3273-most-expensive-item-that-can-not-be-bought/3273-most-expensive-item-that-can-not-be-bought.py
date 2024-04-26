class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        maxNum = primeOne * primeTwo
        bigNum = max(primeOne,primeTwo)
        if primeTwo != bigNum:
            primeOne= primeTwo
            primeTwo = bigNum

        graph = set()
        
        num = 0

        while num < maxNum:
            num+=primeOne
            graph.add(num) 
        
        num = 0
        while num < maxNum:
            num+=primeTwo
            graph.add(num) 

        for i in range(1,(maxNum//primeTwo)):
            num = primeTwo*i
            while num < maxNum:
                num+=primeOne
                graph.add(num)
    
        answer = set([i for i in range(1,maxNum+1)])
        return max(list(answer - graph))