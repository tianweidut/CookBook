class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.result = []
        self._do_psort(arr)
        return self.result
    
    def _do_psort(self, arr):
        if len(arr) <= 1:
            return
        
        max_i, max_v = 0, arr[0]
        for i, v in enumerate(arr):
            if v > max_v:
                max_i, max_v = i, v
                
        self._reverse(arr, max_i)
        self.result.append(max_i + 1)
        
        self._reverse(arr, len(arr) - 1)
        self.result.append(len(arr))
        
        arr.pop()
        self._do_psort(arr)
        
    def _reverse(self, arr, end):
        lo = 0
        hi = end
        
        while lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1