""" https://leetcode.com/problems/counting-bits/
bit manipulation + dp
if lowest bit is 1, then dp[i] = dp[i-1]+1
if lowest bit is 0, then dp[i] = dp[i>>1]
"""
from header import *

# top down


class Solution:
    def countBits(self, n: int) -> List[int]:
        @cache
        def dp(i):
            if i == 0:
                return 0
            elif i & 1:
                return dp(i - 1) + 1
            else:
                return dp(i >> 1)

        return [dp(i) for i in range(n + 1)]

# bottom up


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i & 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp
