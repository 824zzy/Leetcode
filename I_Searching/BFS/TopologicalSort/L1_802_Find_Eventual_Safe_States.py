""" https://leetcode.com/problems/find-eventual-safe-states
translate problem:
    A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
    ==> A node is a safe node if its out degree is 0

twist topological sort to find nodes which out degree is 0
"""
from header import *


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        E = defaultdict(list)
        n = len(graph)
        outD = [0] * n
        for i in range(len(graph)):
            for j in graph[i]:
                E[j].append(i)
                outD[i] += 1

        Q = [i for i, d in enumerate(outD) if d == 0]
        ans = Q.copy()
        while Q:
            i = Q.pop(0)
            for j in E[i]:
                outD[j] -= 1
                if not outD[j]:
                    Q.append(j)
                    ans.append(j)
        return sorted(ans)
