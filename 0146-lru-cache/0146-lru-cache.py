from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        self.nsize = 0
        self.recent = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        if key in self.recent:
            index = self.recent.index(key)
            del self.recent[index]

        self.recent.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            if key in self.recent:
                index = self.recent.index(key)
                del self.recent[index]
        else:
            if self.nsize == self.size:
                del(self.cache[self.recent[0]])
                self.nsize-=1
                if self.recent and self.recent[0] in self.recent:
                    del(self.recent[0])
            else:
                if key in self.recent:
                    index = self.recent.index(key)
                    del self.recent[index]
            self.cache[key] = value
            self.nsize+=1
        
        self.recent.append(key)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)