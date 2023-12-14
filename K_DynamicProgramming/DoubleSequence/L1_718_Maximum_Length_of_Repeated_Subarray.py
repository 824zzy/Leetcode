""" L1: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
A variation of LCS.
Bottom up dp is already very slow, so top down dp is not available.
"""
from header import *

class Solution:
    def findLength(self, A1: List[int], A2: List[int]) -> int:
        dp = [[0 for _ in range(len(A2)+1)] for _ in range(len(A1)+1)]
        ans = 0
        for i in range(len(A1)):
            for j in range(len(A2)):
                if A1[i]==A2[j]: dp[i+1][j+1] = dp[i][j] + 1
                ans = max(dp[i+1][j+1], ans)
        return ans