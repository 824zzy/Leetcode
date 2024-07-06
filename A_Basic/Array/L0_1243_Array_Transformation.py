""" https://leetcode.com/problems/Aay-transformation/
simulation
"""

from header import *


class Solution:
    def transformArray(self, A: List[int]) -> List[int]:
        for _ in count():
            _A = A[:]
            for i in range(1, len(A) - 1):
                if A[i - 1] < A[i] > A[i + 1]:
                    _A[i] -= 1
                if A[i - 1] > A[i] < A[i + 1]:
                    _A[i] += 1
            if _A == A:
                break
            A = _A
        return _A
