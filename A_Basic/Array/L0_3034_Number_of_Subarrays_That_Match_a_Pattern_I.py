""" https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/
brute force to check each subarray
"""
from header import *


class Solution:
    def countMatchingSubarrays(self, A: List[int], P: List[int]) -> int:
        m = len(P)
        ans = 0
        for i in range(len(A) - m):
            for k in range(m):
                if not (A[i + k + 1] > A[i + k] and P[k] == 1) and \
                   not (A[i + k + 1] == A[i + k] and P[k] == 0) and \
                   not (A[i + k + 1] < A[i + k] and P[k] == -1):
                    break
            else:
                ans += 1
        return ans
