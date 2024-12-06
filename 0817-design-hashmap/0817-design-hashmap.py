class MyHashMap:

    def __init__(self):
        self.size = 10007
        self.hashMap = [[] for _ in range(self.size)]

    def hashFunction(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self.hashFunction(key)
        
        for i, (k, v) in enumerate(self.hashMap[hash_key]):
            if k == key:
                self.hashMap[hash_key][i] = (key, value) 
                return
    
        self.hashMap[hash_key].append((key, value))

    def get(self, key: int) -> int:
        hash_key = self.hashFunction(key)
        for k, v in self.hashMap[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hashFunction(key)
        for i, (k, _) in enumerate(self.hashMap[hash_key]):
            if k == key:
                self.hashMap[hash_key].pop(i) 
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)