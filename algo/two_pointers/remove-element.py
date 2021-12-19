class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        i = j = 0
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
