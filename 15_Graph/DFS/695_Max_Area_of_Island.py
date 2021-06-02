""" L1: Graph DFS template
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            grid[x][y] = 0
            cnt = 1
            for dx, dy in neibs:
                if 0<=dx+x<M and 0<=dy+y<N and grid[dx+x][dy+y]==1:
                    cnt += dfs(dx+x, dy+y)
            return cnt
            
        M, N = len(grid), len(grid[0])
        neibs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    ans = max(ans, dfs(i, j))
        return ans