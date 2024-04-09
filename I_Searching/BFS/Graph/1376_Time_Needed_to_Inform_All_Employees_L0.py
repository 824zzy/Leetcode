""" https://leetcode.com/problems/time-needed-to-inform-all-employees/
search along with the maximum time
"""
from header import *

# bfs


class Solution:
    def numOfMinutes(
            self,
            n: int,
            headID: int,
            manager: List[int],
            informTime: List[int]) -> int:
        G = [[] for _ in range(n)]
        for i, x in enumerate(manager):
            if x != -1:
                G[x].append(i)

        Q = [(headID, 0)]
        ans = 0
        while Q:
            i, t = Q.pop(0)
            for j in G[i]:
                Q.append((j, t + informTime[i]))
                ans = max(ans, t + informTime[i])
        return ans

# dfs


class Solution:
    def numOfMinutes(
            self,
            n: int,
            headID: int,
            manager: List[int],
            informTime: List[int]) -> int:
        G = [[] for _ in range(n)]
        for i, x in enumerate(manager):
            if x != -1:
                G[x].append(i)

        def dfs(i, p):
            ans = 0
            for j in G[i]:
                if j != p:
                    ans = max(ans, dfs(j, i))
            return informTime[i] + ans

        return dfs(headID, -1)
