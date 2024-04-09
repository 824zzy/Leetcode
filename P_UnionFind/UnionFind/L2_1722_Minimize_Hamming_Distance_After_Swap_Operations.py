""" https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
dsu + hash table
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
    def minimumHammingDistance(self,
                               S: List[int],
                               T: List[int],
                               A: List[List[int]]) -> int:
        dsu = DSU(len(S))

        for p in A:
            dsu.union(p[0], p[1])

        M = defaultdict(list)
        for i, (x, y) in enumerate(zip(S, T)):
            M[dsu.find(i)].append(i)

        ans = 0
        for k, idx in M.items():
            freq = {}
            for i in idx:
                freq[S[i]] = freq.get(S[i], 0) + 1
                freq[T[i]] = freq.get(T[i], 0) - 1
            ans += sum(x for x in freq.values() if x > 0)
        return ans
