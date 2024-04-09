""" https://leetcode.com/problems/buy-two-chocolates/
reading comprehension, greedily buy the cheapest two chocolates
"""
from header import *

# O(n)


class Solution:
    def buyChoco(self, A: List[int], m: int) -> int:
        x, y = inf, inf
        for a in A:
            if a < x:
                y = x
                x = a
            elif a < y:
                y = a
        s = x + y
        if s <= m:
            m -= s
        return m

# O(nlogn)


class Solution:
    def buyChoco(self, A: List[int], m: int) -> int:
        A.sort()
        if A[0] + A[1] <= m:
            return m - A[0] - A[1]
        else:
            return m
