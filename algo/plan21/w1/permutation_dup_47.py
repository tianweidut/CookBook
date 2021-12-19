class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        track = []
        nums.sort()
        used = [0] * len(nums)
        self.permute(nums, track, used)
        return self.results
    
    def permute(self, nums, track, used):
        if len(track) == len(nums):
            import copy
            self.results.append(copy.copy(track))
            return
        
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                continue
                
            if used[i] == 1:
                continue
                
            track.append(nums[i])
            used[i] = 1
            self.permute(nums, track, used)
            used[i] = 0
            track.pop()