""" https://leetcode.com/problems/minimum-path-sum/submissions/
dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])
"""
# top down solution
class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        @lru_cache(None)
        def dfs(i, j):
            if i==M-1 and j==N-1: return A[i][j]
            if not (0<=i<M and 0<=j<N): return inf
            return A[i][j]+min(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0, 0)
    
    
# bottom up solution
class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i==0 and j==0: dp[i][j] = A[0][0]
                elif i==0: dp[i][j] = A[i][j] + dp[i][j-1]
                elif j==0: dp[i][j] = A[i][j] + dp[i-1][j]
                else: dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]