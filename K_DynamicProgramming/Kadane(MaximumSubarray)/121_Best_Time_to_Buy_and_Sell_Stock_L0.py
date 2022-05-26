""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
minimize buy and maximize profit&loss
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        A = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        ans, cur = -inf, 0
        
        for x in A:
            cur = max(cur+x, x)
            ans = max(ans, cur)
        return max(ans, 0)
    
# bottom up dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1: return 0
        
        A = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        dp = [0] * len(A)
        dp[0] = A[0]
        ans = -inf
        
        for i in range(1, len(A)):
            dp[i] = max(dp[i-1]+A[i], A[i])
        return max(dp+[0])

# top down dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        A = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        
        @cache
        def dp(i):
            if i==len(A): return -inf
            return max(dp(i+1)+A[i], A[i])
        
        return max([0]+[dp(i) for i in range(len(A))])