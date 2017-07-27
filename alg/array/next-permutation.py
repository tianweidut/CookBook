
class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        j = n - 1

        while j > 0 and nums[j] <= nums[j - 1]:
            j -= 1

        if j == 0:
            dn = nums[::-1]
            nums[0:] = dn
            return

        postfix = nums[n - 1:j - 1:-1]
        nums[j:] = postfix
        i = j - 1
        while j < n and nums[j] <= nums[i]:
            j += 1

        nums[j], nums[i] = nums[i], nums[j]
