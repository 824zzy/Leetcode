""" https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
check the length of the target number in the array
"""
from header import *


class Solution:
    def isMajorityElement(self, A: List[int], t: int) -> bool:
        return bisect_right(A, t) - bisect_left(A, t) > len(A) // 2
