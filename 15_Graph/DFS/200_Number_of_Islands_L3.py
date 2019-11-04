# Google
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        
        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c]=='0':
                return
            grid[r][c] = '0'
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
        
        num_islands = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1': 
                    num_islands += 1
                    dfs(grid, r, c)
                    
    return num_islands