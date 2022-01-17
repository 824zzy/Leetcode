""" L1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dfs(i, can):
            if i>=len(A): return 0
            ans = dfs(i+1, can) # skip
            if not can: ans = max(ans, A[i]+dfs(i+2, 1)) # sell
            return max(ans, -A[i]+dfs(i+1, 0)) # buy
        
        return dfs(0, 1)