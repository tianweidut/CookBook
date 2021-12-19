class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        targets = [0] * len(nums)
        
        for n in nums:
            if targets[n] > 0:
                return n
            else:
                targets[n] += 1
                
        return -1