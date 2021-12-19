
class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)

        if len_n <= 2:
            return len_n

        i = j = 0
        while j < len_n:
            cnt = 0
            while j < len_n and nums[j] == nums[i]:
                cnt += 1
                j += 1

            if j == len_n:
                if cnt > 1:
                    nums[i + 1] = nums[i]
                    i += 1
                break

            if j - i != 1:
                if cnt > 1:
                    nums[i + 1] = nums[i]
                    i += 1
                nums[i + 1] = nums[j]
            i += 1

        return i + 1
