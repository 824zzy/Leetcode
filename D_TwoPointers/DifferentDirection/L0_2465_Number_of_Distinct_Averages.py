""" https://leetcode.com/problems/number-of-distinct-averages/description/
sort + two pointers
"""
from header import *


class Solution:
    def distinctAverages(self, A: List[int]) -> int:
        A.sort()
        seen = set()
        l, r = 0, len(A) - 1
        while l < r:
            seen.add((A[l] + A[r]) / 2)
            l += 1
            r -= 1
        return len(seen)
