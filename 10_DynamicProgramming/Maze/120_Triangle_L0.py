""" https://leetcode.com/problems/triangle/
"""
# top down
class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i==len(A) or j==len(A[i]): return 0
            return A[i][j]+min(dfs(i+1, j), dfs(i+1, j+1))
        
        return dfs(0, 0)

# bottom up
class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        dp = A[-1]
        for i in range(len(A)-2, -1, -1):
            for j in range(i+1):
                dp[j] = A[i][j] + min(dp[j], dp[j+1])
        return dp[0]