""" https://leetcode.com/problems/koko-eating-bananas/
check if Koko can eat m bananas in H hours as sentinel
"""
from header import *


class Solution:
    def minEatingSpeed(self, A: List[int], h: int) -> int:
        def fn(k):
            _h = 0
            for x in A:
                _h += ceil(x / k)
            return _h <= h

        l, r = 1, max(A)
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
