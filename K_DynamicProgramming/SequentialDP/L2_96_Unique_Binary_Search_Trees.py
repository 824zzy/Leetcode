""" https://leetcode.com/problems/unique-binary-search-trees
catalan number formula: fn(n) = fn(0)*fn(n-1) + fn(1)*fn(n-2) + ... + fn(n-1)*fn(0)
"""

from header import *


# top down
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(n):
            if n <= 1:
                return 1
            return sum([dp(i) * dp(n - 1 - i) for i in range(n)])

        return dp(n)


# bottom up
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = sum([dp[j] * dp[i - 1 - j] for j in range(i)])
        return dp[-1]
