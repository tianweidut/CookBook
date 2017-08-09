# http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        dmap = {}

        i = 0
        j = 0

        while j < len(nums):
            key = nums[j] / max(1, t)

            for diff in (-1, 0, 1):
                if (key + diff) in dmap and abs(dmap[key + diff] - nums[j]) <= t:
                    return True

            dmap[key] = nums[j]

            if len(dmap) > k:
                dmap.pop(nums[i] / max(1, t))
                i += 1
            j += 1

        return False
