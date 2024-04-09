""" https://leetcode.com/problems/find-in-mountain-array/
1. find peak by ternary search
2. two binary search to find the target
"""
from header import *


class Solution:
    def findInMountainArray(self, t, mountain_arr):
        def fn(x):
            return mountain_arr.get(x)
        # find peak by ternary search
        l, r = 0, mountain_arr.length()
        while l < r:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            if fn(m1) > fn(m2):
                r = m2 - 1
            else:
                l = m1 + 1
        # two binary search to find the target
        peak = l
        ll, rr = 0, peak
        while ll < rr:
            m = (ll + rr) // 2
            x = fn(m)
            if x == t:
                return m
            elif x > t:
                rr = m
            else:
                ll = m + 1

        ll, rr = peak, mountain_arr.length()
        while ll < rr:
            m = (ll + rr) // 2
            x = fn(m)
            if x == t:
                return m
            elif x < t:
                rr = m
            else:
                ll = m + 1
        return -1
