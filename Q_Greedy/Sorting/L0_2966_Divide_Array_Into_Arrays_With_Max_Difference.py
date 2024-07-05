""" https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
"""
from header import *


class Solution:
    def divideArray(self, A: List[int], k: int) -> List[List[int]]:
        A.sort()
        ans = []
        for i in range(0, len(A), 3):
            if A[i + 2] - A[i] > k:
                return []
            ans.append(A[i : i + 3])
        return ans
