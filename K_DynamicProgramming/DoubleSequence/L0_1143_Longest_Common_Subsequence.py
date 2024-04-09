""" https://leetcode.com/problems/longest-common-subsequence/
classical 2d dp problem
"""
from header import *

# top down


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        @cache
        def dp(i, j):
            if i == len(A) or j == len(B):
                return 0
            if A[i] == B[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)

# bottom up


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        for i in reversed(range(len(A))):
            for j in reversed(range(len(B))):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
