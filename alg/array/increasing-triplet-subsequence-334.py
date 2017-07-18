# coding: utf-8


class Solution(object):

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False

        import sys
        num0 = num1 = sys.maxsize

        for n in nums:
            # 当前值若比num0，则必然可以替代num0，这样可以让num0一致是最小的，可以保证后续递增
            # 拥有更多可能性, num1同理，初始时num0,num1都是最大值
            if n <= num0:
                num0 = n
            elif num0 <= n <= num1:
                num1 = n
            else:
                return True

        return False
