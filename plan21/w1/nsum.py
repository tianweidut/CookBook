class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []
        nums.sort()
        track = []
        self.n_sum(nums, 4, 0, target, track)
        return self.results
    
    def n_sum(self, nums, n, start, target, track):
        if n < 2 or start >= len(nums): return
        elif n == 2:
            lo = start
            hi = len(nums) - 1
            
            while lo < hi:
                cal = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                
                if cal == target:
                    self.results.append(track + [left, right])
                    
                    while(lo < hi and nums[lo] == left): lo += 1
                    while(lo < hi and nums[hi] == right): hi -= 1          
                elif cal < target:
                    while(lo < hi and nums[lo] == left): lo += 1
                else:
                    while(lo < hi and nums[hi] == right): hi -= 1
        else:
            i = start
            
            while i < len(nums):
                track.append(nums[i])
                self.n_sum(nums, n-1, i + 1, target - nums[i], track)
                track.pop()
                
                while(i < len(nums) - 1 and nums[i] == nums[i+1]):
                    i+=1
                    
                i += 1
                
                