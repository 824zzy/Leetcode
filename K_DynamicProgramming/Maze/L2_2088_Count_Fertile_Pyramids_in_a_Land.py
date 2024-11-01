""" https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
The idea is the same as 221 and 1277.


1. For each cell, we check if the 3 bottom cell are all 1, if yes, then it is a fertile cell.
2. Then we use minimum of the 3 bottom cells to calculate the number of fertile cells.
Time complexity: O(m*n)
"""

from header import *


class Solution:
    def countPyramids(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])

        @cache
        def dp(i, j):
            if not 0 <= j < n or not 0 <= i < m:
                return 0
            # invalid paramidal vertex
            if G[i][j] == 0:
                return 0
            if (
                i + 1 < m
                and 0 < j < n - 1
                and G[i + 1][j]
                and G[i + 1][j + 1]
                and G[i + 1][j - 1]
            ):
                return min(dp(i + 1, j), dp(i + 1, j + 1), dp(i + 1, j - 1)) + 1
            else:
                return 0

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dp(i, j)
        dp.cache_clear()

        G = G[::-1]
        for i in range(m):
            for j in range(n):
                ans += dp(i, j)
        return ans


"""
[[0,1,1,0],[1,1,1,1]]
[[1,1,1],[1,1,1]]
[[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]
"""
