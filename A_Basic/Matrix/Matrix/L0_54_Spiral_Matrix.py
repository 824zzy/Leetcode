""" https://leetcode.com/problems/spiral-matrix/
Simulate spiral matrix by changing directions.
"""
from header import *


class Solution:
    def spiralOrder(self, M: List[List[int]]) -> List[int]:
        A = []
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        dx, dy = D[d]
        x, y = 0, 0

        for _ in range(len(M) * len(M[0])):
            A.append(M[x][y])
            M[x][y] = inf
            if not (0 <= x + dx < len(M) and 0 <= y + dy <
                    len(M[0])) or M[x + dx][y + dy] == inf:
                d = (d + 1) % 4
                dx, dy = D[d]
            x, y = x + dx, y + dy
        return A
