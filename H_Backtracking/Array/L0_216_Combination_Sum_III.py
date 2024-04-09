""" https://leetcode.com/problems/combination-sum-iii/
The sequal of combination sum with k numbers.
"""
from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        stk = []

        def dfs(x, i):
            if x == n and len(stk) == k:
                return ans.append(stk.copy())
            if x > n:
                return

            for j in range(i, 10):
                stk.append(j)
                dfs(x + j, j + 1)
                stk.pop()

        dfs(0, 1)
        return ans


# itertools


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [l for l in combinations(range(1, 10), k) if sum[l] == n]
