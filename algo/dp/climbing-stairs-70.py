class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1
        q = 2
        
        if n == 1:
            return p
        elif n == 2:
            return q
            
        for i in range(3, n + 1):
            t = p + q
            p = q
            q = t
            
        
        return q
