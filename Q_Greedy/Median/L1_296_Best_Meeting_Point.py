""" https://leetcode.com/problems/best-meeting-point/
greedily find the median of rows and columns
"""
from header import *


class Solution:
    def minTotalDistance(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])
        friends = set([(i, j) for i in range(m) for j in range(n) if G[i][j]])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if G[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        t = [rows[len(rows) // 2], cols[len(cols) // 2]]
        return sum(abs(t[0] - x) + abs(t[1] - y) for x, y in friends)


"""
[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
[[1,1]]
[[1,0,1,0,1]]
"""
