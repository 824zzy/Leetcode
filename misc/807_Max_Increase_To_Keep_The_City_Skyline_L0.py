""" Basic usage of zip(*param) trick
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        LR_skyline, TD_skyline = [], []
        for g in grid:
            LR_skyline.append(max(g))
        for g in zip(*grid):
            TD_skyline.append(max(g))
            
        ans = 0
        for i, lr in enumerate(LR_skyline):
            for j, td in enumerate(TD_skyline):
                ans += min(lr, td) - grid[i][j]
        return ans