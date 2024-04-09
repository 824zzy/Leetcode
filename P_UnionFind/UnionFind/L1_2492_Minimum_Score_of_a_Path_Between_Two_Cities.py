""" https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
1. find the connected components while store the min edge weight
2. find the min edge weight of the component that contains city1
"""
from header import *


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        A = list(range(n + 1))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        mp = defaultdict(lambda: inf)
        for x, y, v in roads:
            union(x, y)
            mp[x] = min(mp[x], v)
            mp[y] = min(mp[y], v)

        target = find(1)
        ans = inf
        for i in range(1, n + 1):
            if find(i) == target:
                ans = min(ans, mp[i])
        return ans
