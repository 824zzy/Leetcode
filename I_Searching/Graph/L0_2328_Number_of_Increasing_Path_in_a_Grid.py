""" https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
dfs with memoization for each cell. 
The solution format is the same as top down dp.

Time complexity: O(m*n)
"""
from header import *

class Solution:
    def countPaths(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        
        @cache
        def dp(x, y):
            ans = 1
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy]>A[x][y]:
                    ans += dp(x+dx, y+dy)%(10**9+7)
            return ans
            
          
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans += dp(i, j)%(10**9+7)
        return ans%(10**9+7)