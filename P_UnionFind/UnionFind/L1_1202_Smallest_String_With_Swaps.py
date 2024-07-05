""" https://leetcode.com/problems/smallest-string-with-swaps/
union find+hash table
use DSU to find character's group and construct result by hash table
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU(len(s))

        for p in pairs:
            dsu.union(p[0], p[1])

        M = defaultdict(list)
        for i in range(len(s)):
            M[dsu.find(i)].append(s[i])
        for k, v in M.items():
            M[k] = sorted(v)
        return "".join([M[p].pop(0) for p in dsu.p])
