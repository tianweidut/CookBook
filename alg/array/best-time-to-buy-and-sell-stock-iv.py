class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cnt = len(prices)
        if cnt <= 1:
            return 0

        if k >= cnt / 2:
            return self.max_profit2(prices)
        
        gp = [0 for i in range(k + 1)]
        lp = [0 for i in range(k + 1)]
        
        i = 1
        while i < cnt:
            diff = prices[i] - prices[i - 1]
            j = k
            while j > 0:
                lp[j] = max(gp[j - 1] + max(0, diff), lp[j] + diff)
                gp[j] = max(gp[j], lp[j])
                j -= 1
            i += 1
        
        return gp[k]
        
    def max_profit2(self, prices):
        r = 0
        i = 1
        while i < len(prices):
            if prices[i] >= prices[i - 1]:
                r += prices[i] - prices[i - 1]
            i += 1
        return r
