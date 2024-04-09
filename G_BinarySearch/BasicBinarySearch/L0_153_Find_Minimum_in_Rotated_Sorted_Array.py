""" https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
non-target binary search.
"""
from header import *


class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] < A[r]:
                r = m
            else:
                l = m + 1
        return A[l]
