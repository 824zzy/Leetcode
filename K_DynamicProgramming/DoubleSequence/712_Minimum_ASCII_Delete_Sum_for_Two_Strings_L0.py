""" https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
"""
from header import *

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        A = list(map(ord, s1))
        B = list(map(ord, s2))
        
        @cache
        def dp(i, j):
            if i==len(s1):
                return sum(B[j:])
            if j==len(s2):
                return sum(A[i:])
            if A[i]==B[j]:
                return dp(i+1, j+1)
            else:
                return min(A[i]+dp(i+1, j), B[j]+dp(i, j+1))
        return dp(0, 0)