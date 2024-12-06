class MyHashMap:

    def __init__(self):
        self.hashMap = [-1 for _ in range(100000)]

    def put(self, key: int, value: int) -> None:
        self.hashMap[hash(key) % 100000] = value

    def get(self, key: int) -> int:
        return self.hashMap[hash(key) % 100000]

    def remove(self, key: int) -> None:
        self.hashMap[hash(key) % 100000] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)