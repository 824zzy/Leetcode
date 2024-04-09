""" https://leetcode.com/problems/longest-palindromic-subsequence/
the same as 1143, a variance of LCS
"""
from header import *

# top down dp solution


class Solution:
    def longestPalindromeSubseq(self, A: str) -> int:
        @cache
        def dp(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if A[i] == A[j]:
                return dp(i + 1, j - 1) + 2
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
        return dp(0, len(A) - 1)

# bottom up dp solution


class Solution:
    def longestPalindromeSubseq(self, A: str) -> int:
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            dp[i][i] = 1

        for i in reversed(range(len(A) - 1)):
            for j in range(i + 1, len(A)):
                if A[i] == A[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
