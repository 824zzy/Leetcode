""" https://leetcode.com/problems/minimum-time-visiting-all-points/
the minimum time between two points: max(dx, dy)
"""
from header import *


class Solution:
    def minTimeToVisitAllPoints(self, A: List[List[int]]) -> int:
        return sum(max(abs(a - x), abs(b - y))
                   for (a, b), (x, y) in pairwise(A))
