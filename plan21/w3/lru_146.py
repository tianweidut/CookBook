class LRUCache:
    
    def __init__(self, capacity: int):
        from collections import deque
        
        self.deque = deque(maxlen=capacity)
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.deque.remove(key)
        self.deque.appendleft(key)
        return self.map[key]
            

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.deque.remove(key)
            self.deque.appendleft(key)
            return
        
        if len(self.map) >= self.capacity:
            rk = self.deque.pop()
            del self.map[rk]
            
        self.map[key] = value
        self.deque.appendleft(key)    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)