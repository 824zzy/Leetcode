""" https://leetcode.com/problems/all-paths-from-source-to-target/
go over the DAG using back tracking
"""
from header import *


class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        ans, stk = [], []

        def dfs(i):
            if i == len(G) - 1:
                return ans.append(stk + [i].copy())
            stk.append(i)
            for j in G[i]:
                dfs(j)
            stk.pop()

        dfs(0)
        return ans
