class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        max_diff = 0
        min_profit = sys.maxsize
        
        for p in prices:
            min_profit = min(p, min_profit)
            max_diff = max(max_diff, p - min_profit)
        
        return max_diff