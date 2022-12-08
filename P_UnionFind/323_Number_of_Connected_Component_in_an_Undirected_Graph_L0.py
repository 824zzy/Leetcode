""" https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
union find template
"""
from header import *

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        A = list(range(n))
        def find(x):
            if A[x]!=x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)

        for i, j in edges:
            union(i, j)
        return len(set(find(i) for i in range(n)))