""" https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
Find lower bound and upper bound by bisect
"""
from header import *

# bisect
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        l = bisect_left(A, t)
        r = bisect_right(A, t)
        if l==r: 
            return [-1, -1]
        else:
            return [l, r-1]