""" https://leetcode.com/problems/check-if-it-is-possible-to-split-array/
Think reversely: check if exist a subarray with a length of 2 that has a sum greater than or equal to 'm'.
"""
from header import *


class Solution:
    def canSplitArray(self, A: List[int], m: int) -> bool:
        if len(A) <= 2:
            return True
        return any(A[i] + A[i + 1] >= m for i in range(len(A) - 1))


"""
[2, 2, 1]
4
[2, 1, 3]
5
[2, 3, 3, 2, 3]
6
"""
