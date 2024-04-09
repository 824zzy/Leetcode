""" https://leetcode.com/problems/paint-house/
classic coloring problem
"""
from header import *


class Solution:
    def minCost(self, A: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == len(A):
                return 0
            ans = inf
            for jj in range(3):
                if jj != j:
                    ans = min(ans, A[i][jj] + dp(i + 1, jj))
            return ans
        return dp(0, None)
