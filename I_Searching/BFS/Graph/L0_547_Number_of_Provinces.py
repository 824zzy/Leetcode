""" https://leetcode.com/problems/number-of-provinces/
dfs template
"""
from header import *


class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        G = defaultdict(dict)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i][j]:
                    G[i][j] = G[j][i] = 1
        seen = set()

        def dfs(i):
            seen.add(i)
            for j in G[i]:
                if j not in seen:
                    dfs(j)

        ans = 0
        for i in range(len(A)):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans
