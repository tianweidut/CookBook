class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums is None or len(nums) == 0 or k < 1:
            return []
        
        queue = MaxQueue(k)
        slide_win = []
        
        for n in nums[0:k-1]:
            queue.push(n)
            
        for n in nums[k-1:]:
            queue.push(n)
            slide_win.append(queue.pop_max())
        
        return slide_win
        
    
class MaxQueue:
    
    from collections import deque
    
    # 单调队列
    def __init__(self, k):
        self.queue = deque()
        self.max_queue = deque()
        
    def push(self, n):
        self.queue.append(n)
        
        while self.max_queue:
            if self.max_queue[-1] < n:
                self.max_queue.pop()
            else:
                self.max_queue.append(n)
                break
                
        if not self.max_queue:
            self.max_queue.append(n)
    
    def pop_max(self):
        max_v = self.max_queue[0]
        v = self.queue.popleft()
        
        if v == max_v:
            self.max_queue.popleft()
            
        return max_v
        
        