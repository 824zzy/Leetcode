""" https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/submissions/
"""
from header import *


class Solution:
    def minIncrements(self, n: int, A: List[int]) -> int:
        def dfs(i):
            if i >= n:
                return 0, 0
            l, l_cost = dfs(2 * i + 1)
            r, r_cost = dfs(2 * i + 2)
            return A[i] + max(l, r), abs(l - r) + l_cost + r_cost

        return dfs(0)[1]
