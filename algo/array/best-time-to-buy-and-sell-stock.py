

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        diff = 0
        s = prices[0]

        for p in prices:
            diff = max(p - s, diff)
            if p <= s:
                s = p

        return diff
