""" https://leetcode.com/problems/longest-common-subsequence/
classical 2d dp problem
"""
# top down
class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        @cache
        def dfs(i, j):
            if i==len(A) or j==len(B): return 0
            if A[i]==B[j]: return 1+dfs(i+1, j+1)
            else: return max(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)
    
# bottom up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(A[i]==B[j]))
        return dp[-1][-1]