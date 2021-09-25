class Solution:
    def singleNumbers2(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) <= 1:
            return []
        
        flag = nums[0]
        for n in nums[1:]:
            flag ^= n
            
        split = 1
        for i in range(0, 32):
            if split & flag == 0:
                split <<= 1
            else:
                break
                
        left, right = [], []
        for n in nums:
            if n & split:
                left.append(n)
            else:
                right.append(n)
                
        left_v = left[0]
        for n in left[1:]:
            left_v ^= n
        
        right_v = right[0]
        for n in right[1:]:
            right_v ^= n 
            
        return [left_v, right_v]
    
    def singleNumbers(self, nums):
        flag, split, left, right = 0, 1, 0, 0
        for n in nums:
            flag ^= n
            
        while (split & flag) == 0:
            split <<= 1
            
        for n in nums:
            if n & split:
                left ^= n
            else:
                right ^= n
                
        return [left, right]