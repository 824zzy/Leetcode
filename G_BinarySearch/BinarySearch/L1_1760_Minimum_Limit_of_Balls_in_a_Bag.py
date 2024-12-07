""" https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
typical binary search problem
"""

from header import *


class Solution:
    def minimumSize(self, A: List[int], maxOperations: int) -> int:
        def fn(x):
            # when penelty is x
            # check if the needed operations is less than maxOperations
            o = 0
            for n in A:
                o += ceil(n / x) - 1
            return o <= maxOperations

        l, r = 1, max(A)
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
