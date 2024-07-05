""" https://leetcode.com/problems/matrix-diagonal-sum/
sum the diagonal
"""
from header import *


class Solution:
    def diagonalSum(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(len(A)):
            ans += A[i][i] + A[i][~i]
        return ans - A[len(A) // 2][len(A) // 2] if len(A[0]) & 1 == 1 else ans
