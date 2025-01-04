import random
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.arr) 
        self.arr.append(val)    
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        idx = self.dic[val]
        last_val = self.arr[-1]

        self.arr[idx] = last_val
        self.dic[last_val] = idx

        self.arr.pop()
        del self.dic[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()