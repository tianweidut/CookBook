class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        nums.sort()
        track = []
        self.subset(nums, 0, track)
        return self.results
        
    def subset(self, nums, start, track):
        import copy
        self.results.append(copy.copy(track))
        
        for i in range(start, len(nums)):
            #同一层的不能重复，下一层的可以重复
            if i > start and nums[i] == nums[i-1]:
                continue
                
            track.append(nums[i])
            self.subset(nums, i + 1, track)
            track.pop()