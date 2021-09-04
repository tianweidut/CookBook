class Deque:
    
    class Node:
        def __init__(self, key=0, val=0, prev=None, next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.head = Deque.Node()
        self.tail = Deque.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
    def appendleft(self, key, val):
        node = Deque.Node(key=key, val=val)
        
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        self.size += 1
        return node
        
    def pop(self):
        if self.size <= 0:
            raise Exception("deque is empty")
        prev = self.tail.prev
        self.remove(prev)
        return prev
    

class LRUCache:
    
    def __init__(self, capacity: int):
        self.deque = Deque()
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.deque.remove(self.map[key])
        node = self.deque.appendleft(key, self.map[key].val)
        self.map[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deque.remove(self.map[key])
            node = self.deque.appendleft(key, value)
            self.map[key] = node
            return
        
        if len(self.map) >= self.capacity:
            rk = self.deque.pop()
            del self.map[rk.key]
            
        node = self.deque.appendleft(key, value)    
        self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)