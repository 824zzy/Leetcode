""" https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid
Find the median
"""
from header import *


class Solution:
    def minOperations(self, A: List[List[int]], x: int) -> int:
        M, N = len(A), len(A[0])
        A = sorted([A[i][j] for j in range(N) for i in range(M)])
        ans = 0
        med = A[len(A) // 2]

        for i in range(len(A)):
            a = abs(med - A[i])
            if a % x:
                return -1
            else:
                ans += a // x
        return ans
