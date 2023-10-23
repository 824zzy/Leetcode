""" https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
1. enumerate on index difference
2. for each index difference, maintain the max and min value in the range of (0, j-idx_diff)
"""
from header import *

class Solution:
    def findIndices(self, A: List[int], idx_diff: int, val_diff: int) -> List[int]:
        mx, mn = 0, 0
        for j in range(idx_diff, len(A)):
            i = j-idx_diff
            if A[i]>A[mx]:
                mx = i
            if A[i]<A[mn]:
                mn = i
            if abs(A[j]-A[mx])>=val_diff:
                return [mx, j]
            if abs(A[j]-A[mn])>=val_diff:
                return [mn, j]
        return [-1, -1]

# binary search
class Solution:
    def findIndices(self, A: List[int], idxDiff: int, valDiff: int) -> List[int]:
        A = [(x, i) for i, x in enumerate(A)]
        A.sort()
        for x, i in A:
            j = bisect_left(A, (x+valDiff, 0))
            for jj in range(j, len(A)):
                if abs(i-A[jj][1])>=idxDiff:
                    return [i, A[jj][1]]
        return [-1, -1]