# coding: utf-8

# 推导:
#	buy[i] = max(buy[i - 1], cold[i - 1] - price)
#	sell[i] = max(sell[i - 1], buy[i - 1] + price)
#   cold[i] = max(sell[i - 1], buy[i - 1], cold[i - 1])

# 演进推导：
#	buy[i] = max(buy[i - 1], sell[i - 2] - price)
#   sell[i] = max(sell[i - 1], buy[i - 1] + price)

# 进一步：buy,sell 至于 i-1, i-2有关


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        import sys
        buy, pre_buy = -sys.maxsize, 0
        sell, pre_sell = 0, 0
        for p in prices:
            pre_buy = buy
            buy = max(buy, pre_sell - p)
            pre_sell = sell
            sell = max(sell, pre_buy + p)

        return sell
