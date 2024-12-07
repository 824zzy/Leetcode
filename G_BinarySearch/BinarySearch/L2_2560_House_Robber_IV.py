""" https://leetcode.com/problems/house-robber-iv/
minimax ==> binary search

use binary search to find the min capability that can rob more than k houses
"""
from header import *


class Solution:
    def minCapability(self, A: List[int], k: int) -> int:
        def fn(t):
            # if min capability can at most rob more than k houses
            f = True
            ans = 0
            for x in A:
                if f:
                    if x <= t:
                        ans += 1
                        f = False
                else:
                    f = True
            return ans >= k

        l, r = 0, max(A)
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
