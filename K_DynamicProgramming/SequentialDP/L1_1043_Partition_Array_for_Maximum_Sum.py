""" https://leetcode.com/problems/partition-array-for-maximum-sum/
sequential dp with K-length window
"""
from header import *


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i >= len(A):
                return 0
            mx = 0
            ans = 0
            for j in range(i, min(i + k, len(A))):
                mx = max(mx, A[j])
                ans = max(ans, (j - i + 1) * mx + dp(j + 1))
            return ans
        return dp(0)
