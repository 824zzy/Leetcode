""" https://leetcode.com/problems/champagne-tower/
2D time sequential dp, the transform equation is:
dp(i, j) = max(0, dp(i-1, j-1)-1)/2 + max(0, dp(i-1, j)-1)/2.
"""
from header import *

# top down


class Solution:
    def champagneTower(self, N: int, R: int, C: int) -> float:
        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return N
            if i < 0 or j > i:
                return 0
            return max(0, dp(i - 1, j - 1) - 1) / 2 + max(0, dp(i - 1, j) - 1) / 2

        return min(dp(R, C), 1)


# bottom up


class Solution:
    def champagneTower(self, N: int, R: int, C: int) -> float:
        dp = [[0 for _ in range(r + 1)] for r in range(R + 1)]
        dp[0][0] = N
        for r in range(R):
            for c in range(r + 1):
                remain = (dp[r][c] - 1) / 2
                if remain > 0:
                    dp[r + 1][c] += remain
                    dp[r + 1][c + 1] += remain
        return min(dp[R][C], 1)
