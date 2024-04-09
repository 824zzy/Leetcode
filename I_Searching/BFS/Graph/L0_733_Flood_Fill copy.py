""" https://leetcode.com/problems/flood-fill/
simple bfs
"""
from header import *


class Solution:
    def floodFill(self, A: List[List[int]], sr: int,
                  sc: int, color: int) -> List[List[int]]:
        Q = [(sr, sc)]
        orig_color = A[sr][sc]
        if orig_color == color:
            return A

        A[sr][sc] = color
        m, n = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while Q:
            x, y = Q.pop(0)
            for dx, dy in D:
                if 0 <= x + dx < m and 0 <= y + \
                        dy < n and A[x + dx][y + dy] == orig_color:
                    A[x + dx][y + dy] = color
                    Q.append((x + dx, y + dy))
        return A
