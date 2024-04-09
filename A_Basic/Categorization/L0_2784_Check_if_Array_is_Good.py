""" https://leetcode.com/problems/check-if-array-is-good/
construct array and compare
"""
from header import *


class Solution:
    def isGood(self, A: List[int]) -> bool:
        A.sort()
        mx = max(A)
        return A == list(range(1, mx + 1)) + [mx]


"""
[2, 1, 3]
[1, 3, 3, 2]
[1, 1]
[3, 4, 4, 1, 2, 1]
[5, 7, 3, 1, 5, 2, 6, 4]
"""
