""" https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
dfs with memoization for each cell. 
The solution format is the same as top down dp.

Time complexity: O(m*n)
"""
from header import *

class Solution:
    def countPaths(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])
        MOD = 10**9+7
        
        @cache
        def dp(x, y):
            ans = 1
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0<=x+dx<m and 0<=y+dy<n and G[x+dx][y+dy]>G[x][y]:
                    ans += dp(x+dx, y+dy)
            return ans%MOD
        
        return sum(dp(i, j) for i, j in product(range(m), range(n)))%MOD