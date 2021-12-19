
class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cnt = len(prices)
        if cnt <= 1:
            return 0

        i = j = 0
        profit = 0

        while j < cnt:
            while j < cnt - 1 and prices[j] <= prices[j + 1]:
                j += 1

            profit += max(0, prices[j] - prices[i])
            j += 1
            i = j

        return profit
