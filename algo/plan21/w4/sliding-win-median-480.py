import heapq as hq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        
        result = []
        
        self.small = []
        self.big = []
        self.small_n = 0
        self.big_n = 0
        self.dmap = defaultdict(int)
        
        left = 0
        for right in range(0, len(nums)):
            if right - left + 1 == k:
                self.add(nums[right])
                result.append(self.median())
                self.remove(nums[left])
                left += 1
            else:
                self.add(nums[right])

        return result
    
    def remove(self, val):
        self.dmap[val] += 1
        if val <= -self.small[0]:
            self.small_n -= 1
        else:
            self.big_n -= 1
    
    def add(self, val):
        if self.small_n == self.big_n:
            hq.heappush(self.big, val)
            
            min_v = hq.heappop(self.big)
            while self.dmap.get(min_v, 0) > 0:
                self.dmap[min_v] -= 1
                min_v = hq.heappop(self.big) 
                
            hq.heappush(self.small, -min_v)
            self.small_n += 1
        else:
            hq.heappush(self.small, -val)
            max_v = -hq.heappop(self.small)
            
            while self.dmap.get(max_v, 0) > 0:
                self.dmap[max_v] -= 1
                max_v = -hq.heappop(self.small)
    
            hq.heappush(self.big, max_v)
            self.big_n += 1
    
    def median(self):
        min_v = -self.small[0]
        while self.dmap.get(min_v, 0) > 0:
            self.dmap[min_v] -= 1
            hq.heappop(self.small)
            min_v = -self.small[0]
        
        if self.small_n == self.big_n:
            max_v = self.big[0]
            while self.dmap.get(max_v, 0) > 0:
                self.dmap[max_v] -= 1
                hq.heappop(self.big)
                max_v = self.big[0]
            return (min_v + max_v) / 2
        else:
            return min_v
        
if __name__ == "__main__":
	#Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
	Solution().medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3)