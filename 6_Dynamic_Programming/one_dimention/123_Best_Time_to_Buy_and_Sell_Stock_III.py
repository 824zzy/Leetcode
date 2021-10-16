""" L1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
buy low & sell high: find minimum buy price and maximum profit&loss
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, pnl = [inf]*2, [0]*2
        for price in prices:
            buy[0] = min(buy[0], price)
            pnl[0] = max(pnl[0], price - buy[0])
            buy[1] = min(buy[1], price - pnl[0])
            pnl[1] = max(pnl[1], price - buy[1])
        return pnl[1]