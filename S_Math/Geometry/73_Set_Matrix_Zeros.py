""" L0
Use col_zero and row_zero to record zero's
"""


class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_zero = []
        row_zero = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not A[i][j]:
                    row_zero.append(i)
                    col_zero.append(j)

        for i in range(len(A)):
            for j in range(len(A[0])):
                if i in row_zero or j in col_zero:
                    A[i][j] = 0
