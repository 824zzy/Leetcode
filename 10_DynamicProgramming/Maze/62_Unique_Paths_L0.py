""" https://leetcode.com/problems/unique-paths/
"""
# bottom up dp
class Solution:
    def uniquePath(self, m:int, n:int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
    
# top down dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n): return 0
            if i==m-1 and j==n-1: return 1
            return dfs(i+1, j)+dfs(i, j+1)
        
        return dfs(0, 0)