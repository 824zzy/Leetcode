""" https://leetcode.com/problems/the-knights-tour/
DO NOT USE self.ans, it will cause TLE
"""
from header import *


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        B = [[-1 for _ in range(n)] for _ in range(m)]
        B[r][c] = 0

        def dfs(x, y, move):
            if move == m * n - 1:
                return True
            for dx, dy in ((1, 2), (1, -2), (-1, 2), (-1, -2),
                           (2, -1), (2, 1), (-2, 1), (-2, -1)):
                if 0 <= x + dx < m and 0 <= y + \
                        dy < n and B[x + dx][y + dy] == -1:
                    B[x + dx][y + dy] = move + 1
                    if dfs(x + dx, y + dy, move + 1):
                        return True
                    B[x + dx][y + dy] = -1
            return False
        dfs(r, c, 0)
        return B
