""" https://leetcode.com/problems/move-zeroes/
exchanges A[i], A[j] if A[j]!=0 and update i
"""
from header import *


class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        i = 0
        for j in range(len(A)):
            if A[j] != 0:
                A[i], A[j] = A[j], A[i]
                i += 1
