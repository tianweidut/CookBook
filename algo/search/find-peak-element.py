
class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        n = len(nums)
        s = 0
        e = n - 1
        while s <= e:
            m = (e - s) / 2 + s

            left = m == 0 or nums[m] > nums[m - 1]
            right = m == n - 1 or nums[m] > nums[m + 1]

            if left and right:
                return m
            elif left:
                s = m + 1
            else:
                e = m - 1
