""" https://leetcode.com/problems/search-a-2d-matrix/
find appropriate row and col indexes by bisect
"""
from header import *


class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        # find appropriate row index
        R = [r[0] for r in A]
        row_idx = bisect_right(R, t) - 1
        # find appropriate col index
        col_idx = bisect_right(A[row_idx], t) - 1
        return (
            0 <= row_idx < len(A)
            and 0 <= col_idx < len(A[0])
            and t == A[row_idx][col_idx]
        )


# another solution: apply binary search on 2D matrix by finding row and
# col indexes by divmod


class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        l, r = 0, len(A) * len(A[0])
        while l < r:
            m = (l + r) // 2
            i, j = divmod(m, len(A[0]))
            if A[i][j] == t:
                return True
            if A[i][j] > t:
                r = m
            else:
                l = m + 1
        return False
