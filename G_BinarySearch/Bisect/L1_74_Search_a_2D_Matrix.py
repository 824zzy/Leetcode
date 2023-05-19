""" https://leetcode.com/problems/search-a-2d-matrix/
find appropriate row and col indexes by bisect
"""
class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        # find appropriate row index
        R = [r[0] for r in A]
        row_idx = bisect_right(R, t)-1
        # find appropriate col index
        col_idx = bisect_right(A[row_idx], t)-1
        return 0<=row_idx<len(A) and 0<=col_idx<len(A[0]) and t==A[row_idx][col_idx]