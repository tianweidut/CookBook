
class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        max_pos = 0
        for pos, step in enumerate(nums):
            if pos <= max_pos:
                max_pos = max(max_pos, pos + step)
            else:
                return False

        return True
