""" https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Find all strongly connected components
"""
from header import *


class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n > len(connections) + 1:
            return -1
        dsu = DSU(n)
        for x, y in connections:
            dsu.union(x, y)
        return len(set([dsu.find(i) for i in range(n)])) - 1
