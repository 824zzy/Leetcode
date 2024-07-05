""" https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
1. sort
2. we
"""
from header import *


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, A: List[int]) -> int:
        A.sort()
        i = 0
        for x in A:
            i = min(x, i + 1)
        return i
