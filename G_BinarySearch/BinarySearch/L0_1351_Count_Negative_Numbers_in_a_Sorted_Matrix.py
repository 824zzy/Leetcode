""" https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
simulation
"""
from header import *


class Solution:
    def countNegatives(self, G: List[List[int]]) -> int:
        ans = 0
        for r in G:
            r.reverse()
            ans += bisect_left(r, 0)
        return ans
