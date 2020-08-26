# Note

## Template

``` py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        def dfs(grid, r, c):
            if `condition`:
                return
            logic over here # grid[r][c] = '0'
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
        `init_varable`
        for r in range(nr):
            for c in range(nc):
                if `condition`:
                    `do sth`
                    dfs(grid, r, c)
        return `ans`
```
