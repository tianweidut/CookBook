class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def s_right(t):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (right - left) // 2 + left
                
                if nums[mid] <= t:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return left
        
        return s_right(target) - s_right(target-1)