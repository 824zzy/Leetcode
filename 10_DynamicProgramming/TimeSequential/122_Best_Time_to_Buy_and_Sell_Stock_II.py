""" L1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
"""
# Top down dp
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dfs(i, canBuy):
            if i==len(A): return 0
            ans = dfs(i+1, canBuy)
            if canBuy:
                ans = max(ans, dfs(i+1, False)-A[i])
            else:
                ans = max(ans, dfs(i+1, True)+A[i])
            return ans
    
        return dfs(0, True)
    
# Bottom up dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        dp[0] = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                dp[i] = dp[i-1] + prices[i]-prices[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]