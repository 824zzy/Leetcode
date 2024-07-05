""" https://leetcode.com/problems/check-knight-tour-configuration/
simulation using bfs
"""
from header import *


class Solution:
    def checkValidGrid(self, A: List[List[int]]) -> bool:
        if A[0][0] != 0:
            return False
        x, y = 0, 0
        D = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        cnt = 0
        seen = {(0, 0)}
        f = True
        while f:
            f = False
            for dx, dy in D:
                if (
                    0 <= x + dx < len(A)
                    and 0 <= y + dy < len(A[0])
                    and (x + dx, y + dy) not in seen
                    and A[x + dx][y + dy] == A[x][y] + 1
                ):
                    cnt += 1
                    seen.add((x + dx, y + dy))
                    x, y = x + dx, y + dy
                    f = True
                    break
        return cnt == len(A) * len(A) - 1
