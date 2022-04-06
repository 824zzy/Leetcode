""" https://leetcode.com/problems/max-area-of-island/
For each cell, apply dfs and mark all cells in island as visit
"""
class Solution:
    def maxAreaOfIsland(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(x, y):
            if not (0<=x<len(A) and 0<=y<len(A[0])) or A[x][y]==0: return 0
            A[x][y] = 0
            area = 0
            for dx, dy in D:
                area += dfs(x+dx, y+dy)
            return 1+area
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans = max(ans, dfs(i, j))
        return ans