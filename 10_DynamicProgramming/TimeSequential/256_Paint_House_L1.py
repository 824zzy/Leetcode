""" https://leetcode.com/problems/paint-house/
top down solution: find minimum cost by checking three colors
"""
class Solution:
    def minCost(self, C: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i<0: return 0
            if j==0: return C[i][j]+min(dfs(i-1, 1), dfs(i-1, 2))
            if j==1: return C[i][j]+min(dfs(i-1, 0), dfs(i-1, 2))
            if j==2: return C[i][j]+min(dfs(i-1, 0), dfs(i-1, 1))
        return min(dfs(len(C)-1, 0), dfs(len(C)-1, 1), dfs(len(C)-1, 2))