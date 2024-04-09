""" https://leetcode.com/problems/find-if-path-exists-in-graph/description/
use union find to check if source and destination are in the same group
"""
from header import *


class Solution:
    def validPath(self,
                  n: int,
                  edges: List[List[int]],
                  source: int,
                  destination: int) -> bool:
        A = list(range(n))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        for i, j in edges:
            union(i, j)
        return find(source) == find(destination)
