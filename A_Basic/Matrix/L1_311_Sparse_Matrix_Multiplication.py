""" https://leetcode.com/problems/sparse-matrix-multiplication/
simulation
"""
from header import *


class Solution:
    def multiply(self, A: List[List[int]],
                 B: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(len(B)):
                if A[i][k]:
                    for j in range(len(B[0])):
                        ans[i][j] += A[i][k] * B[k][j]
        return ans
