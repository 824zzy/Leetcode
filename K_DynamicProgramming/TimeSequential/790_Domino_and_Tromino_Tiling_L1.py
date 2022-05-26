""" https://leetcode.com/problems/domino-and-tromino-tiling/
Find the transitional equation: fn(n) = 2*fn(n-1)+fn(n-3)
"""
class Solution:
    def numTilings(self, N: int) -> int:
        @cache
        def dfs(n):
            if n==1: return 1
            elif n==2: return 2
            elif n==3: return 5
            else: return 2*dfs(n-1)+dfs(n-3)
        
        return dfs(N)%(10**9+7)
