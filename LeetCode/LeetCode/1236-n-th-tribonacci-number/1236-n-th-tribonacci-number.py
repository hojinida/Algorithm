class Solution:
    def tribonacci(self, n: int) -> int:
        tn = [0 for _ in range(38)]
        tn[0]=0
        tn[1]=1
        tn[2]=1

        for i in range(3,n+1):
            tn[i]=tn[i-1]+tn[i-2]+tn[i-3]
        
        return tn[n]