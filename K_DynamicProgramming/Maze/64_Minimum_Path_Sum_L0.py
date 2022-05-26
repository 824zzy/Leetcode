""" https://leetcode.com/problems/minimum-path-sum/submissions/
dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])
"""
# top down solution
class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        @cache
        def dfs(i, j):
            if i==M-1 and j==N-1: return A[i][j]
            if not (0<=i<M and 0<=j<N): return inf
            return A[i][j]+min(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)
    
    
# bottom up solution
class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        dp = [[inf for j in range(len(A[0])+1)] for i in range(len(A)+1)]
        dp[0][1] = dp[1][0] = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(A[0])+1):
                dp[i][j] = A[i-1][j-1]+min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]