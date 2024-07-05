""" https://leetcode.com/problems/walls-and-gates/
"""
from header import *


class Solution:
    def wallsAndGates(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(A), len(A[0])
        Q = [(i, j) for i in range(m) for j in range(n) if A[i][j] == 0]

        D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = 1
        while Q:
            nxtQ = []
            for x, y in Q:
                for dx, dy in D:
                    if (
                        0 <= x + dx < m
                        and 0 <= y + dy < n
                        and A[x + dx][y + dy] == 2147483647
                    ):
                        A[x + dx][y + dy] = step
                        nxtQ.append((x + dx, y + dy))
            step += 1
            Q = nxtQ
