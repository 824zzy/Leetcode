""" https://leetcode.com/problems/solving-questions-with-brainpower/
knapsack problem: at each index we just need to decide add integer or not
"""
from header import *


class Solution:
    def mostPoints(self, A: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(A):
                return 0
            return max(dp(i + 1), A[i][0] + dp(i + A[i][1] + 1))

        return dp(0)


class Solution:
    def mostPoints(self, A: List[List[int]]) -> int:
        dp = [0] * (len(A) + 1)
        for i in reversed(range(len(A))):
            p, b = A[i]
            dp[i] = max(dp[i + 1], p + dp[min(i + b + 1, len(A))])
        return dp[0]
