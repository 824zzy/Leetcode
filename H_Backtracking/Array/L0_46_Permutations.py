""" https://leetcode.com/problems/permutations/
back tracking with remained elements
"""
from header import *


class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        ans = []
        stk = []

        def dfs(A):
            if not A:
                return ans.append(stk.copy())
            for i, x in enumerate(A):
                stk.append(x)
                dfs(A[:i] + A[i + 1:])
                stk.pop()

        dfs(A)
        return ans
