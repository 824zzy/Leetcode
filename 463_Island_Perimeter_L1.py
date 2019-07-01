class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n, nums, conn = len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    nums += 1
                    if i>0 and grid[i-1][j]==1:
                        conn += 1
                    if i<m-1 and grid[i+1][j] ==1:
                        conn += 1
                    if j>0 and grid[i][j-1]==1:
                        conn += 1
                    if j<m-1 and grid[i][j+1]==1:
                        conn += 1
        
        return 4*nums-conn