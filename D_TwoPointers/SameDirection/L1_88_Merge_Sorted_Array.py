""" https://leetcode.com/problems/merge-sorted-array/
two pointers + reverse thinking

assign values from end to start using two pointers
"""
from header import *


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n = m - 1, n - 1
        for k in reversed(range(m + n + 2)):
            if m < 0:
                A[k] = B[n]
                n -= 1
            elif n < 0:
                A[k] = A[m]
                m -= 1
            elif A[m] < B[n]:
                A[k] = B[n]
                n -= 1
            else:
                A[k] = A[m]
                m -= 1
