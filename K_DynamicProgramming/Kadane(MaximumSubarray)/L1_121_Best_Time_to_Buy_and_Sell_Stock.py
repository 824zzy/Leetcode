""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
minimize buy and maximize profit
"""
from header import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = inf
        ans = 0
        for p in prices:
            mn = min(mn, p)
            ans = max(ans, p-mn)
        return ans
    

# bottom up dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        A = [y-x for x, y in pairwise(prices)]
        dp = [0]*len(A)
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = max(A[i]+dp[i-1], A[i])
        return max(dp)


# top down dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        A = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        
        @cache
        def dp(i):
            if i==len(A): return -inf
            return max(dp(i+1)+A[i], A[i])
        
        return max([0]+[dp(i) for i in range(len(A))])
    

# 0-1 knapsack (suboptimal)
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dp(i, can):
            if i==len(A): return 0
            ans = dp(i+1, can) # skip
            if not can: ans = max(ans, A[i]) # sell
            return max(ans, -A[i]+dp(i+1, 0)) # buy
        
        return dp(0, 1)
    

# greedily find the minimum and maximum
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, mx = inf, -inf
        A, B = [], []
        for x, y in zip(prices, prices[::-1]):
            mn = min(mn, x)
            mx = max(mx, y)
            A.append(mn)
            B.append(mx)
        ans = 0
        for a, b in zip(A, B[::-1]):
            ans = max(ans, b-a)
        return ans