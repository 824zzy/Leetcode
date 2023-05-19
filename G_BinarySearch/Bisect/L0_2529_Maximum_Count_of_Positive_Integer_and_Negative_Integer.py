""" https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
find position of 0
"""
from header import *

class Solution:
    def maximumCount(self, A: List[int]) -> int:
        i = bisect_left(A, 0)
        j = bisect_right(A, 0)
        return max(i, len(A)-j)
        