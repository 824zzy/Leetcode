""" https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
1. find groups
2. count size of every group
3. count unreachable pairs
"""
from header import *


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        A = list(range(n + 1))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        for i, j in edges:
            union(i, j)

        cnt = Counter()
        for i in range(n):
            cnt[find(i)] += 1

        ans = 0
        for k, v in cnt.items():
            ans += v * (n - v)
        return ans // 2
