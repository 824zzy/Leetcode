""" https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
binary search on the speed, and check if the time sum is valid.
"""
from header import *


class Solution:
    def minSpeedOnTime(self, A: List[int], hour: float) -> int:
        def fn(x):
            h = 0
            for i in range(len(A) - 1):
                h += ceil(A[i] / x)
            return h + A[-1] / x <= hour

        l, r = 1, 10 ** 7 + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l if l != 10 ** 7 + 1 else -1
