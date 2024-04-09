""" https://leetcode.com/problems/flood-fill/
simple dfs
"""
from header import *


class Solution:
    def floodFill(self,
                  A: List[List[int]],
                  sr: int,
                  sc: int,
                  newColor: int) -> List[List[int]]:
        origColor = A[sr][sc]
        if origColor == newColor:
            return A
        m, n = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            A[x][y] = newColor
            for dx, dy in D:
                if 0 <= x + dx < m and 0 <= y + \
                        dy < n and A[x + dx][y + dy] == origColor:
                    dfs(x + dx, y + dy)

        dfs(sr, sc)
        return A
