# coding: utf-8
# 多数投票算法


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major1 = major2 = None
        cnt1 = cnt2 = 0

        for n in nums:
            if n == major1:
                cnt1 += 1
            elif n == major2:
                cnt2 += 1
            elif cnt1 == 0:
                major1 = n
                cnt1 = 1
            elif cnt2 == 0:
                major2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for n in nums:
            if n == major1:
                cnt1 += 1
            elif n == major2:
                cnt2 += 1

        r = []
        len_n = len(nums)
        if cnt1 > len_n / 3.0:
            r.append(major1)
        if cnt2 > len_n / 3.0:
            r.append(major2)

        return r
