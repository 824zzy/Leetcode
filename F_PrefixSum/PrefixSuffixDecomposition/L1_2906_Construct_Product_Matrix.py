""" https://leetcode.com/problems/construct-product-matrix/
2D version of 238
"""
from header import *


class Solution:
    def constructProductMatrix(self, A: List[List[int]]) -> List[List[int]]:
        prefix = [[1 for _ in range(len(A[0]))] for _ in range(len(A))]
        suffix = [[1 for _ in range(len(A[0]))] for _ in range(len(A))]
        suf = 1
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(A[0]) - 1, -1, -1):
                suffix[i][j] = suf
                suf = suf * A[i][j] % 12345

        pre = 1
        for i in range(len(A)):
            for j in range(len(A[0])):
                prefix[i][j] = pre
                pre = pre * A[i][j] % 12345

        ans = [[None for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans[i][j] = prefix[i][j] * suffix[i][j] % 12345
        return ans
