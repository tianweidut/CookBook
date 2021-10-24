class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import heapq
        
        queue = [-v for v in arr[:k]]
        heapq.heapify(queue)
        
        for v in arr[k:]:
            heapq.heappushpop(queue, -v)
            
        return [-v for v in queue]