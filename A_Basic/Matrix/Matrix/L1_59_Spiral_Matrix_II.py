""" https://leetcode.com/problems/spiral-matrix-ii/
be careful when change direction
"""
from header import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0 for _ in range(n)] for _ in range(n)]
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0
        dx, dy = D[d]

        for i in range(1, n * n + 1):
            A[x][y] = i
            if not (0 <= x + dx < n and 0 <= y + dy <
                    n and A[x + dx][y + dy] == 0):
                d = (d + 1) % 4
                dx, dy = D[d]
            x, y = x + dx, y + dy
        return A
