""" https://leetcode.com/problems/minimum-falling-path-sum/
variation of Pascal's triangle
dp[i][j] = A[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
"""
from header import *

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if not 0<=j<len(A[0]): return inf
            if i==len(A)-1: return A[i][j]
            return A[i][j]+min(dp(i+1, j-1), dp(i+1, j), dp(i+1, j+1))
        
        return min(dp(0, j) for j in range(len(A[0])))
    

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        for i in reversed(range(len(A)-1)):
            for j in range(len(A[0])):
                l = dp[i+1][j-1] if j-1>=0 else inf
                m = dp[i+1][j]
                r = dp[i+1][j+1] if j+1<len(A[0]) else inf
                dp[i][j] += min(l, m, r)
        return min(dp[0])