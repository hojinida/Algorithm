class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        pattern = [1]

        i = 2
        while i <= len1 and i <= len2:
            if len1%i == 0 and len2%i == 0:
                pattern.append(i)
            i+=1
        
        pattern.sort(reverse=True)

        flag = True
        answer = None
        for p in pattern:
            jug = str1[0:p]
            for i in range(len1 // p):
                if str1[i*p:i*p+p] != jug:
                    flag =False
                    break
            
            for i in range(len2 // p):
                if str2[i*p:i*p+p] != jug:
                    flag =False
                    break
            
            if flag :
                return jug
        
        return ""

        