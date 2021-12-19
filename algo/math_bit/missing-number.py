
class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_n = n * (n - 1) / 2

        flag = False
        for i in nums:
            if i < n:
                sum_n -= i

            if i == 0:
                flag = True

        return n if flag and sum_n == 0 else sum_n
