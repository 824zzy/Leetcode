""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
three states: skip / sell / buy with fee
"""
from header import *

class Solution:
    def maxProfit(self, A: List[int], fee: int) -> int:
        @cache
        def dp(i, canBuy):
            if i==len(A):
                return 0
            ans = dp(i+1, canBuy)  # do nothing
            if canBuy: # buy
                ans = max(ans, dp(i+1, False)-A[i]-fee)
            else:
                ans = max(ans, dp(i+1, True)+A[i])
            return ans
        
        return dp(0, True)
    
class Solution:
    def maxProfit(self, A: List[int], f: int) -> int:
        dp_s = [0] * len(A)
        dp_h = [0] * len(A)
        dp_h[0] = -A[0]
        for i in range(1, len(A)):
            dp_s[i] = max(dp_s[i-1], dp_h[i-1]+A[i]-f)
            dp_h[i] = max(dp_h[i-1], dp_s[i-1]-A[i])
        return dp_s[-1]