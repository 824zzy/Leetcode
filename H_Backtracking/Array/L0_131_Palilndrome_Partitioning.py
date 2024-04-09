""" https://leetcode.com/problems/palindrome-partitioning/
since s.length<=16, just backtracking is enough
"""
from header import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        stk = []

        def dfs(i):
            if i == len(s):
                return ans.append(stk.copy())
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    stk.append(s[i:j])
                    dfs(j)
                    stk.pop()
        dfs(0)
        return ans
