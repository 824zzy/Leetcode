""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
buy/sell/skip
"""
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dp(i, can):
            if i==len(A): return 0
            ans = dp(i+1, can) # skip
            if not can: ans = max(ans, A[i]) # sell
            return max(ans, -A[i]+dp(i+1, 0)) # buy
        
        return dp(0, 1)