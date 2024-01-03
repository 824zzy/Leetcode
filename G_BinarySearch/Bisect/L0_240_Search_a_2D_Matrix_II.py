""" https://leetcode.com/problems/search-a-2d-matrix-ii/
binary search to find the row and column
"""
from header import *

# O(mlogn)
class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        _A = zip(*A)
        for i in range(bisect_right(list(_A)[0], t)):
            j = bisect_left(A[i], t)
            if j<len(A[0]) and A[i][j]==t:
                return True
        return False
        
# start from bottom left corner and search the target
# O(max(m, n))
class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        i, j = len(A)-1, 0
        while 0<=i<len(A) and 0<=j<len(A[0]):
            if A[i][j]==t:
                return True
            if A[i][j]>t:
                i -= 1
            else:
                j += 1
        return False
            