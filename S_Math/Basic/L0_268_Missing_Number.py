""" https://leetcode.com/problems/missing-number/
Gaussian summation
"""
from header import *


class Solution:
    def missingNumber(self, A: List[int]) -> int:
        n = len(A)
        t = n * (n + 1) // 2
        return t - sum(A)
