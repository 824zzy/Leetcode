""" https://leetcode.com/problems/largest-submatrix-with-rearrangements/
1. use histogram model to count continuous 1 on each column
2. sort the histogram model to update ans

Time complexity: O(m*n*logn)
"""
from header import *


class Solution:
    def largestSubmatrix(self, A: List[List[int]]) -> int:
        ans = 0
        hist = [0] * len(A[0])

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    hist[j] += 1
                else:
                    hist[j] = 0
            for k, x in enumerate(sorted(hist, reverse=True)):
                ans = max(ans, x * (k + 1))
        return ans
