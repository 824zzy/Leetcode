""" L0: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
minimize buy and maximize profit&loss
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy, pnl = float('inf'), 0
        for p in prices:
            buy = min(buy, p)
            pnl = max(pnl, p-buy)
        return pnl
    
# dp solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        dp = [0] * len(prices)
        dp[0] = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(prices[i]-min_p, dp[i-1])
            min_p = min(prices[i], min_p)
        return dp[-1]