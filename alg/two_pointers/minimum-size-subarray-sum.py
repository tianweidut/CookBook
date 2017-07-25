class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = j = 0
        cur_sum = 0
        len_n = len(nums)
        min_distance = len_n + 1

        while j < len(nums):
            cur_sum += nums[j]

            while cur_sum >= s:
                if j - i + 1 < min_distance:
                    min_distance = j - i + 1

                cur_sum -= nums[i]
                i += 1
            j += 1

        return min_distance if min_distance != len_n + 1 else 0
