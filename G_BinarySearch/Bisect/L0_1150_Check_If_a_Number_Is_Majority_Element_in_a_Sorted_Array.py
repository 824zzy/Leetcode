""" https://leetcode.com/problems/most-frequent-even-element/
use binary search to find the left and right boundary of the target
"""
from header import *


class Solution:
    def isMajorityElement(self, A: List[int], t: int) -> bool:
        return bisect_right(A, t) - bisect_left(A, t) > len(A) // 2
