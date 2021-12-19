
class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        len_n = len(nums)
        i = k = 0
        j = len_n - 1

        while k <= j:
            while nums[k] == 2 and k < j:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1

            while nums[k] == 0 and i < k:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1

            k += 1
