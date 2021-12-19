class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        
        nums.sort()
            
        results = []
        for i, v in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            while start < end:
                target = v + nums[start] + nums[end]
                if target == 0:
                    results.append([v, nums[start], nums[end]])
                    start += 1
                    while(start < end and nums[start] == nums[start-1]): start += 1 
                    
                elif target > 0:
                    end -= 1
                else:
                    start += 1
            
        return results