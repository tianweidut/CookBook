
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        import sys
        front = 1
        back = 1
        max_product = - sys.maxint - 1
        
        i = 0
        cnt = len(nums)
        while i < cnt:
            front *= nums[i]
            back *= nums[cnt - 1 - i]
            max_product = max(front, back, max_product)
            
            if front == 0:
                front = 1
            if back == 0:
                back = 1
            
            i += 1
            
        return max_product
