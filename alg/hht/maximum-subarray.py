
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if not nums:
            return None

        max_n = nums[0]
        sum_n = 0

        for n in nums:
            sum_n += n
            max_n = max(max_n, sum_n)

            if sum_n < 0:
                sum_n = 0

        return max_n
