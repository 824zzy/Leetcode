""" https://leetcode.com/problems/powx-n/
Binary Exponentiation technique
"""
from header import *


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def dq(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1 / x
            if n & 1:
                return dq(n // 2) * dq(n // 2 + 1)
            else:
                return dq(n // 2) * dq(n // 2)

        return dq(n)


"""
2.00000
10
2.10000
3
2.00000
-2
0.44528
0
8.66731
4
"""
