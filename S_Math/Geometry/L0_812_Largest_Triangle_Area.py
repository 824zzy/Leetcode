""" https://leetcode.com/problems/largest-triangle-area/
brute force follow the formula of area of triangle:
    area = 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)
"""
from header import *


class Solution:
    def largestTriangleArea(self, A: List[List[int]]) -> float:
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                for k in range(j + 1, len(A)):
                    x1, y1 = A[i][0], A[i][1]
                    x2, y2 = A[j][0], A[j][1]
                    x3, y3 = A[k][0], A[k][1]
                    ans = max(ans, abs(x1 * y2 + x2 * y3 + x3 *
                              y1 - y1 * x2 - y2 * x3 - y3 * x1) / 2)
        return ans
