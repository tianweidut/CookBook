class Solution:
    def minArray(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = (end - start)//2 + start
            
            if nums[end] == nums[mid]:
                end = end - 1
            elif nums[end] > nums[mid]:
                end = mid
            else:
                start = mid + 1
                
        return nums[start]
        