""" https://leetcode.com/problems/graph-valid-tree/
check circle by union find
"""
from header import *


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        A = list(range(n))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        for x, y in edges:
            if find(x) == find(y):
                return False
            union(x, y)
        return len(set([find(i) for i in range(n)])) == 1
