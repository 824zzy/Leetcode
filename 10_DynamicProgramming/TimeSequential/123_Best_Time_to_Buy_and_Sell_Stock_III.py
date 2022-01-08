""" L1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
buy low & sell high: find minimum buy price and maximum profit&loss
"""
# top down solution
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dfs(i, canBuy):
            if i==len(A) or not canBuy: return 0
            ans = dfs(i+1, canBuy) # skip
            if canBuy>0:
                ans = max(ans, dfs(i+1, -1*(canBuy-1))-A[i])
            elif canBuy<0:
                ans = max(ans, dfs(i+1, -1*canBuy)+A[i])
            return ans
        
        return dfs(0, 3)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, pnl = [inf]*2, [0]*2
        for price in prices:
            buy[0] = min(buy[0], price)
            pnl[0] = max(pnl[0], price - buy[0])
            buy[1] = min(buy[1], price - pnl[0])
            pnl[1] = max(pnl[1], price - buy[1])
        return pnl[1]