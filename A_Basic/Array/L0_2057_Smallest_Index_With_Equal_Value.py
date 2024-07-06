""" https://leetcode.com/problems/smallest-index-with-equal-value/
array simulation
"""

from header import *


class Solution:
    def smallestEqual(self, A: List[int]) -> int:
        for i, v in enumerate(A):
            if i % 10 == v:
                return i
        return -1
