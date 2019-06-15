class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ans = 0
        for r in range(grid):
            for c in range(grid[0]):
                if grid[r][c] == 1:
                    ans = max(ans, self.dfs(grid, r, c))
        return ans

    def dfs(self, grid: List[List[int]], r: int, c: int) -> int:
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
            return 0
        
        grid[r][c] = 0
        island = 1
        island += self.dfs(grid, r+1, c)
        island += self.dfs(grid, r-1, c)
        island += self.dfs(grid, r, c+1)
        island += self.dfs(grid, r, c-1)
        return island