
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        k = 3
        min_n = []
        max_n = []
        heapq.heapify(min_n)
        heapq.heapify(max_n)
        
        for n in nums:
            if n < 0:
                if len(min_n) < k:
                    heapq.heappush(min_n, -n)
                elif min_n[0] < -n:
                    heapq.heappushpop(min_n, -n)
                    
            if len(max_n) < k:
                heapq.heappush(max_n, n)
            elif max_n[0] < n:
                heapq.heappushpop(max_n, n)
                    
        min_n = sorted([-n for n in min_n])
        max_n = sorted(max_n)
        
        print max_n
        print min_n
        
        max_v = max_n[0] * max_n[1] * max_n[2]
        if len(min_n) < 2:
            return max_v
        else:
            return max(max_v, min_n[0] * min_n[1] * max_n[-1])
            
