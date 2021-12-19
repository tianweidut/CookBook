
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dmap = {}
        
        for n in nums:
            if n not in dmap:
                dmap[n] = 1
            else:
                return True
            
        return False
