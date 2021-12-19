class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = max([res[j] + 1 for j in range(0, i) if nums[i] > nums[j]] or [1])
            
        return max(res)