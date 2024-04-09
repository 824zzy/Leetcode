""" https://leetcode.com/problems/rotate-image/
1. basic usage of zip(*param)
2. flip by diagonal and row
"""
from header import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(zip(*matrix)):
            matrix[i] = list(row[::-1])


class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # flip by diagonal
        for i in range(len(A)):
            for j in range(i, len(A[0])):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        # flip by row
        for i in range(len(A)):
            A[i] = A[i][::-1]
