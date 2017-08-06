
# http://www.cnblogs.com/grandyang/p/4281975.html


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cnt = len(prices)
        if cnt <= 1:
            return 0

        k = 2
        gp = [[0] * (k + 1) for i in range(cnt + 1)]
        lp = [[0] * (k + 1) for i in range(cnt + 1)]

        i = 1
        while i < cnt:
            diff = prices[i] - prices[i - 1]
            j = 1
            while j <= k:
                lp[i][j] = max(
                    gp[i - 1][j - 1] + max(0, diff), lp[i - 1][j] + diff)
                gp[i][j] = max(gp[i - 1][j], lp[i][j])
                j += 1
            i += 1

        return gp[cnt - 1][k]
