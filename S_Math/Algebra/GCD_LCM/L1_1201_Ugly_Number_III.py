""" https://leetcode.com/problems/ugly-number-iii/
Given x, the ugly number less or equal than x can be found by inclusion-exclusion principle:
    multiple of a or b or c - multiple of lcm(a,b) - multiple of lcm(a,c) - multiple of lcm(b, c) + multiple of lcm(a, b, c)

x = 10, a = 2, b = 4, c = 6, lcm(a,b) = 4, lcm(a,c) = 6, lcm(b,c) = 12, lcm(a, b, c) = 12
a: 2 4 6 8 10
b: 4 8
c: 6
"""
from header import *


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def fn(x):
            # return True if there are n ugly numbers less than x
            cnt = (
                x // a
                + x // b
                + x // c
                - x // lcm(a, b)
                - x // lcm(b, c)
                - x // lcm(a, c)
                + x // lcm(a, b, c)
            )
            return cnt >= n

        a, b, c = sorted([a, b, c])
        l = min(a, b, c)
        r = min(a, b, c) * n + 1

        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
