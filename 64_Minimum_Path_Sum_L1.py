# First column and raw!
""" Classical Two dimensional dynamic programming
Note that dont initialize by multiply list : dp = [[0] * n] * m
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Edge Case
        if not grid:
            return 0 
        # Build DP Matrix
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        # Case 1
        for r in range(1, m):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        # Case 2
        for c in range(1, n):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        # The rest
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        
        return dp[-1][-1]