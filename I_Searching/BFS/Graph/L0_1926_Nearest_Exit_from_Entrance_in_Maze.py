""" https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
BFS template
"""
from header import *


class Solution:
    def nearestExit(self, A: List[List[str]], entrance: List[int]) -> int:
        x0, y0 = entrance
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        Q = [(0, x0, y0)]
        seen = set()
        seen.add((x0, y0))
        while Q:
            step, x, y = Q.pop(0)
            if (x == 0 or x == len(A) - 1 or y == 0 or y ==
                    len(A[0]) - 1) and [x, y] != entrance:
                return step
            for dx, dy in D:
                if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]) and (
                        x + dx, y + dy) not in seen and A[x + dx][y + dy] == '.':
                    seen.add((x + dx, y + dy))
                    Q.append((step + 1, x + dx, y + dy))
        return -1
