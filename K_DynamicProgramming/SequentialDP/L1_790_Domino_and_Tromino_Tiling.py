""" https://leetcode.com/problems/domino-and-tromino-tiling/
Find the transitional equation: dp(n) = 2*dp(n-1)+dp(n-3)
"""
from header import *


class Solution:
    def numTilings(self, N: int) -> int:
        @cache
        def dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n == 3:
                return 5
            else:
                return 2 * dp(n - 1) + dp(n - 3)

        return dp(N) % (10 ** 9 + 7)


class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10 ** 9 + 7)
        return dp[-1] % (10 ** 9 + 7)
