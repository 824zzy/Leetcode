""" https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
linear scan to find the largest positive integer that exists with its negative by a set
"""
from header import *


class Solution:
    def findMaxK(self, A: List[int]) -> int:
        A.sort()
        seen = set()
        ans = -1
        for x in A:
            if -x in seen:
                ans = x
            seen.add(x)
        return ans
