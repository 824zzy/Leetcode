""" https://leetcode.com/problems/find-peak-element/description/
when A[m]>A[m+1], the peak must be in [l, m], because A[m+1] is decreasing
when A[m]<A[m+1], the peak must be in [m+1, r], because A[m] is increasing
"""
from header import *


class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] > A[m + 1]:
                r = m
            else:
                l = m + 1
        return l
