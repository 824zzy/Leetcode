""" https://leetcode.com/problems/longest-consecutive-sequence/
1. union all consecutive element pairs
2. find maximum size of disjoint set

Time complexity: O(n)
"""


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
    def longestConsecutive(self, A: List[int]) -> int:
        A = set(A)
        dsu = DSU(len(A))
        # compress A in mp
        mp = {x: i for i, x in enumerate(A)}
        for x in A:
            if x - 1 in mp:
                dsu.union(mp[x - 1], mp[x])
            if x + 1 in mp:
                dsu.union(mp[x + 1], mp[x])
        freq = Counter([dsu.find(mp[x]) for x in A])
        return max(freq.values(), default=0)
