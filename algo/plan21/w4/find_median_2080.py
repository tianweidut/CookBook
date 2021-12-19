import heapq as hq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []


    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            hq.heappush(self.right, num)
            val = hq.heappop(self.right)
            hq.heappush(self.left, -val)
        else:
            hq.heappush(self.left, -num)
            val = hq.heappop(self.left)
            hq.heappush(self.right, -val)
            


    def findMedian(self) -> float:        
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()