""" https://leetcode.com/problems/climbing-stairs/
dp[i-1] + dp[i-2]
"""
from header import *

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# top down solution
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i==2: return 2
            if i==1: return 1
            return dp(i-1)+dp(i-2)
        
        return dp(n)