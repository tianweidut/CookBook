
class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        if len_n <= 1:
            return len_n

        i = j = 0
        while j < len_n:

            while j < len_n and nums[j] == nums[i]:
                j += 1

            if j == len_n:
                break

            if j - i != 1:
                nums[i + 1] = nums[j]
            i += 1

        return i + 1
