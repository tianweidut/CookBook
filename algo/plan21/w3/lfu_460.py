class LFUCache:
    
    class Node:
        def __init__(self, key, val, freq=1):
            self.key = key
            self.val = val
            self.freq = freq
    
    def __init__(self, capacity: int):
        from collections import deque, defaultdict
        
        self.map = {}
        self.freq_map = defaultdict(deque)
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        val = self.map[key].val
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <=0:
            return
        
        if key in self.map:
            n = self.map[key]
            n.val = value
            
            freq_deque = self.freq_map[n.freq]
            freq_deque.remove(key)
            
            if len(freq_deque) == 0:
                del self.freq_map[n.freq]
                
            n.freq += 1
            self.freq_map[n.freq].appendleft(key)
            self.min_freq = min(self.freq_map)
            return
        
        if len(self.map) >= self.capacity:
            freq_deque = self.freq_map[self.min_freq]
            k = freq_deque.pop()
            del self.map[k]
            if len(freq_deque) == 0:
                del self.freq_map[self.min_freq]
                
        n = LFUCache.Node(key, value, 1)
        self.freq_map[n.freq].appendleft(key)
        self.map[key] = n
        self.min_freq = n.freq


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)