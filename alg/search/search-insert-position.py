

class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        s = 0
        e = len(nums) - 1

        while s <= e:
            m = (e - s) / 2 + s

            if nums[m] == target:
                return m
            elif target < nums[m]:
                e = m - 1
            else:
                s = m + 1

        return max(e + 1 if target > nums[e] else e, 0)
