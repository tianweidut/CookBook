class MaxQueue:

    def __init__(self):
        from collections import deque
        
        self.queue = deque()
        self.max_queue = deque()

    def max_value(self) -> int:
        return self.max_queue[0] if self.max_queue else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        
        while self.max_queue:
            if self.max_queue[-1] < value:
                self.max_queue.pop()
            else:
                self.max_queue.append(value)
                break
                
        if not self.max_queue:
            self.max_queue.append(value)
        
    def pop_front(self) -> int:
        if not self.queue:
            return -1
        
        val = self.queue.popleft()
        if val == self.max_queue[0]:
            self.max_queue.popleft()
            
        return val