""" https://leetcode.com/problems/guess-number-higher-or-lower-ii/
"""
from header import *

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(i, j):
            if i>=j: return 0
            ans = inf
            for k in range(i, j+1):
                ans = min(ans, k+max(dp(i, k-1), dp(k+1, j)))
            return ans
            
        return dp(1, n)