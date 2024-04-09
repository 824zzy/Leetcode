""" https://leetcode.com/problems/non-decreasing-subsequences/
backtracking using set to avoid duplicates
"""
from header import *


class Solution:
    def findSubsequences(self, A: List[int]) -> List[List[int]]:
        stk = []
        ans = set()

        def dfs(i):
            if len(stk) > 1:
                ans.add(tuple(stk.copy()))
            for j in range(i + 1, len(A)):
                if A[i] <= A[j]:
                    stk.append(A[j])
                    dfs(j)
                    stk.pop()

        for i in range(len(A)):
            stk = [A[i]]
            dfs(i)
        return ans
