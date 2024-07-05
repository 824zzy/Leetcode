""" https://leetcode.com/problems/is-graph-bipartite/
the same as 886,
classical bipartite problem:
1. traverse the graph by bfs
2. check if any node has painted the same color
"""
from header import *

# bfs solution


class Solution:
    def isBipartite(self, G: List[List[int]]) -> bool:
        seen = {}

        for i in range(len(G)):
            if i not in seen:
                Q = [(i, 1)]
                while Q:
                    i, color = Q.pop(0)
                    for j in G[i]:
                        if j not in seen:
                            seen[j] = -color
                            Q.append((j, -color))
                        elif seen[j] * color > 0:
                            return False
        return True


# dfs solution


class Solution:
    def isBipartite(self, G: List[List[int]]) -> bool:
        seen = {}

        def dfs(i, color):
            if i in seen:
                return seen[i] * color > 0
            seen[i] = color
            return all(dfs(j, -color) for j in G[i])

        return all(dfs(i, 1) for i in range(len(G)) if i not in seen)


# union find solution


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def isBipartite(self, A: List[List[int]]) -> bool:
        dsu = DSU(len(A))
        for i, nodes in enumerate(A):
            ii = dsu.find(i)
            for j in nodes:
                jj = dsu.find(j)
                # if i and j belong to the same group, the graph is not
                # bipartite
                if ii == jj:
                    return False
                dsu.union(nodes[0], j)
        return True
