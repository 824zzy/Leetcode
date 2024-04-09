""" https://leetcode.com/problems/apply-operations-to-an-array/description/
brute force simulation
"""
from header import *


class Solution:
    def applyOperations(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                A[i] *= 2
                A[i + 1] = 0
        ans = [x for x in A if x != 0]
        return ans + [0] * (len(A) - len(ans))
