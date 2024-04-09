""" https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
sort the array
"""
from header import *


class Solution:
    def canMakeArithmeticProgression(self, A: List[int]) -> bool:
        if len(A) == 2:
            return True
        A.sort()
        for i in range(1, len(A) - 1):
            if A[i + 1] - A[i] != A[i] - A[i - 1]:
                return False
        return True
