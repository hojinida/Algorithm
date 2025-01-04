from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # 가장 최근에 사용된 항목으로 이동
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)  # 가장 오래된 항목 제거


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)