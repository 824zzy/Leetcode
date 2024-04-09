""" https://leetcode.com/problems/sort-the-matrix-diagonally/
1. build diagonal hash table
2. sort the diagonal array
3. reconstruct matrix
"""
from header import *


class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        diag = defaultdict(SortedList)
        for i in range(m):
            for j in range(n):
                diag[i - j].add(A[i][j])

        for i in range(m):
            for j in range(n):
                A[i][j] = diag[i - j].pop(0)

        return A
