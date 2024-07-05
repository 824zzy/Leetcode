""" https://leetcode.com/problems/cherry-pickup-ii/
maze dp simulation
"""
from header import *


class Solution:
    def cherryPickup(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])

        @cache
        def dp(i, j1, j2):
            if i == m:
                return 0
            if not (0 <= j1 < n) or not (0 <= j2 < n):
                return -inf
            ans = 0
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    v = G[i][j1] + G[i][j2] if j1 != j2 else G[i][j1]
                    ans = max(ans, v + dp(i + 1, j1 + d1, j2 + d2))
            return ans

        return dp(0, 0, n - 1)
