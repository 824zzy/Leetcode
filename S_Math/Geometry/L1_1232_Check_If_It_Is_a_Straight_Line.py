""" https://leetcode.com/problems/check-if-it-is-a-straight-line/
Check if three points are colinear using cross product
(x0 - x1) * (y1 - y2) - (y0 - y1) * (x1 - x2) == 0.
"""
from header import *

class Solution:
    def checkStraightLine(self, A: List[List[int]]) -> bool:
        x0, y0 = A[0]
        x1, y1 = A[1]
        for x2, y2 in A[2:]:
            if (x0-x1)*(y1-y2)!=(x1-x2)*(y0-y1):
                return False
        return True

# brute force: check every two points are colinear
class Solution:
    def checkStraightLine(self, A: List[List[int]]) -> bool:
        n = len(A)
        k = None
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = A[i]
                x2, y2 = A[j]
                if y1==y2:
                    return all(y==y1 for x, y in A)
                if not k:
                    k = (x2-x1)/(y2-y1)
                elif (x2-x1)/(y2-y1)!=k:
                    return False
        return True