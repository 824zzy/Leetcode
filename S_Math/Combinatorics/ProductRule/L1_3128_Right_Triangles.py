""" https://leetcode.com/problems/right-triangles/
rule of product of rows and columns with more than 1 '1'
"""

from header import *


class Solution:
    def numberOfRightTriangles(self, G: List[List[int]]) -> int:
        R = [x.count(1) for x in G]
        C = [x.count(1) for x in zip(*G)]

        ans = 0
        for i in range(len(R)):
            for j in range(len(C)):
                if G[i][j] and R[i] > 1 and C[j] > 1:
                    ans += (R[i] - 1) * (C[j] - 1)
        return ans


"""
[[0,1,0],[0,1,1],[0,1,0]]
[[1,0,0,0],[0,1,0,1],[1,0,0,0]]
[[1,0,1],[1,0,0],[1,0,0]]
"""
