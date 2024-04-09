""" https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
greedy sort the closest pair of x-axis points
"""
from header import *


class Solution:
    def maxWidthOfVerticalArea(self, A: List[List[int]]) -> int:
        return max([j - i for (i, _), (j, _) in pairwise(sorted(A))])
