""" https://leetcode.com/problems/peak-index-in-a-mountain-array/
Ternary search template
"""
from header import *


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def fn(x):
            return A[x]

        l, r = 0, len(A)
        while l < r:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            if fn(m1) > fn(m2):
                r = m2 - 1
            else:
                l = m1 + 1
        return l


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def fn(x):
            return A[x]

        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if fn(m) > fn(m + 1):
                r = m
            else:
                l = m + 1
        return l
