
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dmap = {}

        for pos, val in enumerate(nums):
            if val not in dmap:
                dmap[val] = pos
            else:
                if pos - dmap[val] <= k:
                    return True
                else:
                    dmap[val] = pos
        return False
