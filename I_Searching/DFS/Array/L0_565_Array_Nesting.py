""" https://leetcode.com/problems/array-nesting/
dfs on array
"""
from header import *

class Solution:
    def arrayNesting(self, A: List[int]) -> int:
        def dfs(x):
            if x in seen:
                return 0
            seen.add(x)
            return 1+dfs(A[x])
        
        seen = set()
        ans = 0
        for x in A:
            if x in seen: continue
            ans = max(ans, dfs(x))
        return ans