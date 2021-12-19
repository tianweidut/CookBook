
class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        i = 0
        steps = 0
        while i < n:
            farthest_pos = i + nums[i]

            if farthest_pos == i:
                return 0
            elif farthest_pos >= n - 1:
                steps += 1
                break

            j = i
            max_pos = 0
            next_pos = i
            while j <= farthest_pos and j < n:
                if j + nums[j] > max_pos:
                    max_pos = j + nums[j]
                    next_pos = j
                j += 1

            i = next_pos
            steps += 1

        return steps
