class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1,p2 = 0 , len(s)-1
        flag1=True
        flag2=True
        while p1<=p2:
            if s[p1] == s[p2]:
                p1+=1
                p2-=1
            else:
                tp1, tp2 = p1+1, p2
                while tp1<=tp2:
                    if s[tp1] == s[tp2]:
                        tp1+=1
                        tp2-=1
                    else:
                        flag1=False
                        break
                
                tp1, tp2 = p1, p2-1
                while tp1<=tp2:
                    if s[tp1] == s[tp2]:
                        tp1+=1
                        tp2-=1
                    else:
                        flag2=False
                        break
                break
        if flag1 or flag2:
            return True
        else:
            return False

