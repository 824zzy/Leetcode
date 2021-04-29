""" basic usage of zip(*param)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(zip(*matrix)):
            # Note that row type is tuple
            matrix[i] = list(row[::-1])


""" Transform and rotate
"""         
class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(A)):
            for j in range(i, len(A[0])):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(len(A)): A[i] = A[i][::-1]