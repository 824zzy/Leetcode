""" https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/
binary search + math

Observation: suppose d1=4, d2=6
arr1 = 1 2 3   5 6 7   9 10 11   13 ...
arr2 = 1 2 3 4 5   7 8 9 10 11   13 ...
1. arr1 contains: all the numbers - multiple of 4
2. arr2 contains: all the numbers - multiple of 6
3. arr1 and arr2 both contain: not multiple of 4 and 6 = all the numbers - multiple of LCM(4,6)=12

worse case for upper bound: d1 = d2 = 2, only odd numbers are allowed, so the upper bound is 2*(u1+u2)
"""
from header import *


class Solution:
    def minimizeSet(self, d1: int, d2: int, u1: int, u2: int) -> int:
        def fn(x):
            # return true if there are at least u1 and u2 numbers in arr1 and
            # arr2 and their count sum is at least x
            if u1 <= x - x // d1 and u2 <= x - x // d2 and u1 + u2 <= x - x // _lcm:
                return True
            else:
                return False

        l, r = 0, 2 * (u1 + u2)
        _lcm = lcm(d1, d2)
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
