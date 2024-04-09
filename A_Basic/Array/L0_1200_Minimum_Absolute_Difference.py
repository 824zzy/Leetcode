""" https://leetcode.com/problems/minimum-absolute-difference/
keep track of minimal difference of each pair
"""
from header import *


class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        mn = min(b - a for a, b in pairwise(A))
        return [[a, b] for a, b in pairwise(A) if b - a == mn]
