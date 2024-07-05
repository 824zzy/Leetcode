""" https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
post order traversal on all the nodes along with the distance and the flag of whether the node's subtree has apple
"""
from header import *


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        def dfs(i, p):
            t = 0
            f = hasApple[i]
            for j in G[i]:
                if j != p:
                    _t, _f = dfs(j, i)
                    t += _t
                    f |= _f
            if i == 0:
                return t
            return t + 2 * f, f

        return dfs(0, None)
