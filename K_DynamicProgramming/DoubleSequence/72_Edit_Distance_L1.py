""" https://leetcode.com/problems/edit-distance/
Delete: dfs(i+1, j) + 1
Insert: dfs(i, j+1) + 1
Replace: dfs(i+1, j+1) + 1
"""
from header import *

class Solution:
    def minDistance(self, A: str, B: str) -> int:
        @cache
        def dfs(i, j):
            if i==len(A) or j==len(B): return len(A)+len(B)-i-j
            if A[i]==B[j]: return dfs(i+1, j+1)
            return 1+min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
        
        return dfs(0, 0)