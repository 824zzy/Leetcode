""" https://leetcode.com/problems/search-a-2d-matrix/
apply binary search on 2D matrix by finding row and col indexes by divmod
"""
class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        l, r = 0, len(A)*len(A[0])
        while l<r:
            m = (l+r)//2
            i, j = divmod(m, len(A[0]))
            if A[i][j]==t: return True
            if A[i][j]>t: r = m
            else: l = m+1
        return False