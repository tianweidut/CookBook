
class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import math
        n = len(nums)
        ps = int(math.pow(2, n))
        nums = sorted(nums)
        r = []

        for i in range(0, ps):
            sub = []

            cnt = 0
            while i:
                if i & 1:
                    sub.append(nums[cnt])
                i = i >> 1
                cnt += 1

            if sub not in r:
                r.append(sub)

        return r
