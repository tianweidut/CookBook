
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        cnt = len(nums)
        left = [0] * cnt
        right = [0] * cnt
        
        max_n = nums[0]
        sum_n = 0
        for i in range(cnt):
            sum_n += nums[i]
            max_n = max(max_n, sum_n)
            sum_n = max(0, sum_n)
            left[i] = max_n
            
        max_n = nums[-1]
        sum_n = 0
        for i in range(cnt - 1, -1, -1):
            sum_n += nums[i]
            max_n = max(max_n, sum_n)
            sum_n = max(0, sum_n)
            right[i] = max_n
            
        import sys
        max_n = - sys.maxint - 1
        for i in range(cnt - 1):
            max_n = max(max_n, left[i] + right[i+1])
            
        return max_n
            
