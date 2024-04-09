""" https://leetcode.com/problems/fibonacci-number/
classical textbook problem
"""
from header import *

# bottom up solution


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

# top down solution


class Solution:
    def fib(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            return dp(i - 1) + dp(i - 2)
        return dp(n)
