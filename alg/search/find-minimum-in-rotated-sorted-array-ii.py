

class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = len(nums) - 1

        while s <= e:
            m = (e - s) / 2 + s

            if nums[m] == nums[s] == nums[e]:
                return min(nums[s: e + 1])
            elif nums[s] <= nums[m] <= nums[e]:
                return nums[s]
            elif nums[s] <= nums[m]:
                s = m + 1
            else:
                e = m

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = len(nums) - 1

        while s < e:
            m = (e - s) / 2 + s

            if nums[m] > nums[e]:
                s = m + 1
            elif nums[m] < nums[e]:
                e = m
            else:
                e -= 1
        return nums[s]
