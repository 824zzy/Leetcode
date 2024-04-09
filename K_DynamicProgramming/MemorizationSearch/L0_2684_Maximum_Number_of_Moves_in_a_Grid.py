""" https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
"""
from header import *


class Solution:
    def maxMoves(self, G: List[List[int]]) -> int:
        @cache
        def dp(x, y):
            ans = 0
            for dx, dy in ((-1, 1), (0, 1), (1, 1)):
                if 0 <= x + dx < len(G) and 0 <= y + \
                        dy < len(G[0]) and G[x][y] < G[x + dx][y + dy]:
                    ans = max(ans, 1 + dp(x + dx, y + dy))
            return ans

        ans = 0
        for i in range(len(G)):
            ans = max(ans, dp(i, 0))
        return ans
