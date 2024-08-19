""" https://leetcode.com/problems/maximum-number-of-points-with-cost/
Intuition: dp(i, j) is the maximum score we can get starting from row i, column j.
We can go left, right, or stay in the same column.

Share the same idea with the problem 1014. Best Sightseeing Pair.
"""

from header import *


class Solution:
    def maxPoints(self, M: List[List[int]]) -> int:
        m, n = len(M), len(M[0])

        @cache
        def dp(i, j):
            if i == m:
                return 0
            ans = M[i][j] + max(dp_left(i + 1, j), dp_right(i + 1, j))
            return ans

        @cache
        def dp_left(i, j):
            if j == 0:
                return dp(i, j)
            return max(dp(i, j), dp_left(i, j - 1) - 1)

        @cache
        def dp_right(i, j):
            if j == n - 1:
                return dp(i, j)
            return max(dp(i, j), dp_right(i, j + 1) - 1)

        return max(dp(0, j) for j in range(n))
