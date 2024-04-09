""" https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
brute force
"""
from header import *


class Solution:
    def longestMonotonicSubarray(self, A: List[int]) -> int:
        ans = 1
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                for j in range(i, len(A) - 1):
                    if A[j] < A[j + 1]:
                        ans = max(ans, j - i + 2)
                    else:
                        break
            elif A[i] > A[i + 1]:
                for j in range(i, len(A) - 1):
                    if A[j] > A[j + 1]:
                        ans = max(ans, j - i + 2)
                    else:
                        break
        return ans


"""
[1,4,3,3,2]
[3,3,3,3]
[3,2,1]
"""
