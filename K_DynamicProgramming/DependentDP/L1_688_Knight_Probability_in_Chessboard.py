""" https://leetcode.com/problems/knight-probability-in-chessboard/
"""
from header import *


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dp(x, y, kk):
            if not (0 <= x < n and 0 <= y < n):
                return 0
            if kk == 0:
                return 1
            ans = 0
            for dx, dy in (
                (2, 1),
                (2, -1),
                (1, 2),
                (1, -2),
                (-1, 2),
                (-1, -2),
                (-2, 1),
                (-2, -1),
            ):
                ans += dp(x + dx, y + dy, kk - 1) / 8
            return ans

        return dp(row, column, k)
