class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)

        while i < n:
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

            i += 1

        j = 0
        while j < n:
            if nums[j] != j + 1:
                return j + 1
            j += 1

        return j + 1
