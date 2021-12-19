class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        m = 1
        ones = 0
        
        while m <= n:
            a, b = divmod(n, m)
            ones += a / 10 * m
            c = a % 10
            if c == 1:
                ones += b + 1
            elif c > 1:
                ones += m
            m *= 10
        return ones
            
        
