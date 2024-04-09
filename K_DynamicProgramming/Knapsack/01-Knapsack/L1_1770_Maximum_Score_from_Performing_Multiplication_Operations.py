""" https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
pick elements from the front or the end of the array

Time complexity: O(n^2)
"""
from header import *


class Solution:
    def maximumScore(self, A: List[int], M: List[int]) -> int:
        n, m = len(A), len(M)
        dp = [[0] * m for _ in range(m + 1)]

        for i in reversed(range(m)):
            for j in range(i, m):
                k = i + m - j - 1
                dp[i][j] = max(A[i] * M[k] + dp[i + 1][j],
                               A[j - m + n] * M[k] + dp[i][j - 1])

        return dp[0][-1]


# Top down is not working due to TLE
class Solution:
    def maximumScore(self, A: List[int], M: List[int]) -> int:
        @cache
        def dp(i, j, idx):
            if idx == len(M):
                return 0
            return max(M[idx] * A[i] + dp(i + 1, j, idx + 1),
                       M[idx] * A[j] + dp(i, j - 1, idx + 1))

        return dp(0, len(A) - 1, 0)
