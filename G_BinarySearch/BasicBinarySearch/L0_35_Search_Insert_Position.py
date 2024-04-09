""" https://leetcode.com/problems/search-insert-position/
binary search template
"""
from header import *


class Solution:
    def searchInsert(self, A: List[int], target: int) -> int:
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] >= target:
                r = m
            else:
                l = m + 1
        return l
