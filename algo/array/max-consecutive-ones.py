class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcnt = 0
        cnt = 0
        
        for n in nums:
            if n == 1:
                cnt += 1
                maxcnt = max(cnt, maxcnt)
            else:
                cnt = 0
                
        return maxcnt
        
