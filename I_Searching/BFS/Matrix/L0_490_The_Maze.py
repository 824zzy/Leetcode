""" https://leetcode.com/problems/the-maze/
bfs on matrix, only add the cell to seen when it is the end of the path
"""
from header import *


class Solution:
    def hasPath(self, M: List[List[int]], s: List[int], d: List[int]) -> bool:

        Q = [s]
        seen = {tuple(s)}
        while Q:
            x, y = Q.pop(0)
            if [x, y] == d:
                return True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xx, yy = x, y
                while (
                    0 <= xx + dx < len(M)
                    and 0 <= yy + dy < len(M[0])
                    and M[xx + dx][yy + dy] == 0
                ):
                    xx, yy = xx + dx, yy + dy
                if (xx, yy) not in seen:
                    Q.append((xx, yy))
                    seen.add((xx, yy))
        return False


"""
[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
[0,4]
[4,4]
[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
[0,4]
[3,2]
[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
[4,3]
[0,1]
"""
