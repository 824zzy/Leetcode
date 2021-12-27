""" https://leetcode.com/problems/minimum-falling-path-sum/
variation of Pascal's triangle
dp[i][j] = A[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
"""
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        @lru_cache(None)
        def dfs(i, j):
            if i==n: return 0
            if not (0<=j<n): return inf
            return A[i][j]+min(dfs(i+1, j-1), dfs(i+1, j), dfs(i+1, j+1))
        
        return min(dfs(0, j) for j in range(n))
    

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        A = [[float('inf')]+a+[float('inf')] for a in A]
        M, N = len(A), len(A[0])
        dp = [[float('inf') for _ in range(N)] for _ in range(M)]
        
        dp[0] = A[0]
        for i in range(1, M):
            for j in range(1, N-1):
                dp[i][j] = A[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
                
        return min(dp[-1])
