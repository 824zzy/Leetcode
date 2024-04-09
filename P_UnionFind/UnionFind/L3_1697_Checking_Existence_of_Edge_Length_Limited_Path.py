""" https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
1. sort queries and edgeList based on weights
2. add edges whose weight less then query's weight to DSU
3. check if query's nodes are in the same set a.k.a connected.
"""
from header import *


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
    def distanceLimitedPathsExist(self,
                                  n: int,
                                  edgeList: List[List[int]],
                                  queries: List[List[int]]) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        dsu = DSU(n)
        ans = [0] * len(queries)
        for w, i, j, idx in queries:
            while edgeList and edgeList[0][0] < w:
                _, ii, jj, = edgeList.pop(0)
                dsu.union(ii, jj)
            if dsu.find(i) == dsu.find(j):
                ans[idx] = True
            else:
                ans[idx] = False
        return ans
