
class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        s = 0
        e = len(nums) - 1

        while s <= e:
            m = (e - s) / 2 + s

            if nums[s] <= nums[m] <= nums[e]:
                return nums[s]
            elif nums[s] <= nums[m]:
                s = m + 1
            else:
                e = m
