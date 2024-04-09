""" https://leetcode.com/problems/neither-minimum-nor-maximum/
simulate
"""
from header import *


class Solution:
    def findNonMinOrMax(self, A: List[int]) -> int:
        mx, mn = max(A), min(A)
        for x in A:
            if x != mx and x != mn:
                return x
        else:
            return -1
