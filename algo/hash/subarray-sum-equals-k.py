

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        from collections import defaultdict

        d = defaultdict(int)
        d[0] = 1
        psum = 0
        cnt = 0

        for n in nums:
            psum += n
            cnt += d[psum - k]
            d[psum] += 1

        return cnt
