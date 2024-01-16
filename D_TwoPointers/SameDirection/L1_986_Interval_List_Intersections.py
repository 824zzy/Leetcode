""" https://leetcode.com/problems/interval-list-intersections/
Define two pointers to scan through A and B respectively. If the intervals overlap, put the overlapped part in ans. 
Otherwise, increment the pointer for the interval that ends ahead.
"""
from header import *

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i<len(A) and j<len(B):
            l = max(A[i][0], B[j][0])
            r = min(A[i][1], B[j][1])
            if l<=r:
                ans.append([l, r])
            if A[i][1]<B[j][1]: # move i, j based on end time
                i += 1
            else:
                j += 1
        return ans