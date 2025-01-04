class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5:0 , 10:0}

        for bill in bills:
            if bill == 10:
                if money[5] < 1:
                    return False
                money[10]+=1
                money[5]-=1
            elif bill == 20:
                if money[5] >= 1 and money[10] >= 1:
                    money[5]-=1
                    money[10]-=1
                elif money[5] >= 3:
                    money[5]-=3
                else:
                    return False   
            else:
                money[5]+=1

        return True