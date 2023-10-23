""" https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
brute force for the small data size: O(n^2)
"""
from header import *

class Solution:
    def findIndices(self, A: List[int], idx_diff: int, val_diff: int) -> List[int]:
        for i in range(len(A)):
            for j in range(i+idx_diff, len(A)):
                if abs(A[i]-A[j])>=val_diff:
                    return [i, j]
        return [-1, -1]