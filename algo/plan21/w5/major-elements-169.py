class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return None
        
        val = nums[0]
        freq = 1
        
        for n in nums[1:]:
            if freq == 0:
                val = n
                freq = 1
            else:
                freq = freq + (1 if n == val else -1)
                
        return val