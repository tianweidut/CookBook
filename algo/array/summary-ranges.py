class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        i = 0
        j = 1
        cnt = len(nums)
        r = []
        
        def _add(s, e):
            if s == e:
                r.append("%s" % nums[s])
            else:
                r.append("%s->%s" % (nums[s], nums[e]))
        
        while j < cnt:
            if nums[j] - nums[j-1] != 1:
                _add(i, j - 1)
                i = j        
            j += 1
        
        _add(i, j - 1)
        return r
        
        
