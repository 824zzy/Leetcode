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