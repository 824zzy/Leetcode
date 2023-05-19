""" https://leetcode.com/problems/delete-operation-for-two-strings/
two solution:
1. directly find minimum operations to delete characters
2. find longest common subsequence and indirectly compute the minimum operations
"""
from header import *

# top down for #1
class Solution:
    def minDistance(self, A: str, B: str) -> int:
        @cache
        def dp(i, j):
            if i==len(A) and j==len(B): return 0
            elif i==len(A): return len(B)-j
            elif j==len(B): return len(A)-i
            
            if A[i]==B[j]: return dp(i+1, j+1)
            else: return 1+min(dp(i+1, j), dp(i, j+1))
        
        return dp(0, 0)
  
    
# top down for #2
class Solution:
    def minDistance(self, A, B):
        @cache
        def dp(i, j):
            if i < 0 or j < 0: return 0
            if A[i] == B[j]: return dp(i-1,j-1) + 1
            else: return max(dp(i-1,j), dp(i,j-1))

        m, n = len(A), len(B)
        return m + n - 2*dp(m-1, n-1)
    
    
# bottom up for #1
class Solution:
    def minDistance(self, A: str, B: str) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(len(B)+1): dp[0][i] = i
        for j in range(len(A)+1): dp[j][0] = j
            
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]!=B[j]: dp[i+1][j+1] = 1+min(dp[i][j+1], dp[i+1][j])
                else: dp[i+1][j+1] = dp[i][j]
        return dp[-1][-1]


# bottom up for #2
class Solution:
    def minDistance(self, A: str, B: str) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]: dp[i+1][j+1] = dp[i][j]+1
                else: dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return len(A)+len(B)-2*dp[-1][-1]