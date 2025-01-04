import random
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = 0
        self.length+=1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        del(self.dic[val])
        self.length-=1
        return True

    def getRandom(self) -> int:
        pick = random.randrange(0,self.length)
        return list(self.dic.keys())[pick]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()