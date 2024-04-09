""" https://leetcode.com/problems/edit-distance/
Delete: dfs(i+1, j) + 1
Insert: dfs(i, j+1) + 1
Replace: dfs(i+1, j+1) + 1
"""
from header import *


class Solution:
    def minDistance(self, A: str, B: str) -> int:
        @cache
        def dp(i, j):
            if i == len(A):
                return len(B) - j
            if j == len(B):
                return len(A) - i
            if A[i] == B[j]:
                return dp(i + 1, j + 1)
            else:
                # replace
                ans = 1 + dp(i + 1, j + 1)
                # delete/insert
                ans = min(ans, 1 + dp(i + 1, j), 1 + dp(i, j + 1))
                return ans
        return dp(0, 0)
