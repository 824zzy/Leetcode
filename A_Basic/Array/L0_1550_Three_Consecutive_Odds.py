""" https://leetcode.com/problems/three-consecutive-odds/
array simulation
"""
from header import *


class Solution:
    def threeConsecutiveOdds(self, A: List[int]) -> bool:
        for i in range(len(A) - 2):
            if A[i] & 1 and A[i + 1] & 1 and A[i + 2] & 1:
                return True
        return False
