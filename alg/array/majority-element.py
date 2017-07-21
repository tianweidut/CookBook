
class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        num = None
        cnt = 0

        for n in nums:
            if cnt >= len(nums) / 2 + 1:
                break

            if num is None:
                num = n
                cnt = 1
            elif num == n:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    num = None

        return num
