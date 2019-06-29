# First column and raw!
""" Classical Two dimensional dynamic programming
Note that dont initialize by multiply list : dp = [[0] * n] * m
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 

        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                
        return grid[-1][-1]