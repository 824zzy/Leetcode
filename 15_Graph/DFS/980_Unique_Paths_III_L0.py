from copy import deepcopy
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        ob = sum([1 for r in grid for c in r if c==-1])
        def dfs(grid, r, c, s):
            if r<0 or r>=nr or c<0 or c>=nc or grid[r][c]==-1:                    
                return
            if grid[r][c]==2 and s==nr*nc-ob:
                self.ans += 1
                return
            cpgrid = deepcopy(grid)
            cpgrid[r][c] = -1
                
            dfs(cpgrid, r-1, c, s+1)
            dfs(cpgrid, r+1, c, s+1)
            dfs(cpgrid, r, c-1, s+1)
            dfs(cpgrid, r, c+1, s+1)
        
        self.ans = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]==1:
                    dfs(grid, r, c, 1)
        return self.ans