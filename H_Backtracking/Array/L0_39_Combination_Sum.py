""" https://leetcode.com/problems/combination-sum/
use backtracking to find all combination sum and break statement for pruning
"""
from header import *


class Solution:
    def combinationSum(self, A: List[int], t: int) -> List[List[int]]:
        stk = []
        ans = []

        def dfs(i, sm):
            if sm > t:
                return
            if sm == t:
                ans.append(stk.copy())
                return
            for j in range(i, len(A)):
                x = A[j]
                stk.append(x)
                dfs(j, sm + x)
                stk.pop()

        dfs(0, 0)
        return ans
