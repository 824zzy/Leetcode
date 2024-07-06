""" https://leetcode.com/problems/convert-1d-array-into-2d-array/
simulation: use n as stride
"""

from header import *


class Solution:
    def construct2DArray(self, A: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(A):
            return []
        ans = []
        for i in range(0, len(A), n):
            ans.append(A[i : i + n])
        return ans
